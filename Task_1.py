import psycopg2
import json
import xml.etree.ElementTree as ET
import os
import logging
import time
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from enum_Type import outputFormat
from dotenv import load_dotenv

time.sleep(10)
load_dotenv()

logging.basicConfig(level = logging.INFO,filename = "task1_log.log",filemode = "w",
                    format = "%(asctime)s %(levelname)s %(message)s")

class Database:
 def __init__(self):
    self.dbname = os.getenv('DATABASE_DBNAME')
    self.user = os.getenv('DATABASE_USER')
    self.password = os.getenv('DATABASE_PASSWORD')
    self.host = os.getenv('DATABASE_HOST')
    self.port = os.getenv('DATABASE_PORT')

 def connectDatabase(self):
    try:
      self.conn = psycopg2.connect(dbname = self.dbname,user=self.user,password=self.password,host=self.host,port=self.port)
      logging.info("Database connected successfully")
     
    except psycopg2.OperationalError:
      logging.error("Connection error",exc_info=True)
      
    except UnicodeDecodeError:
      logging.error("Problems with dbname,user or password",exc_info = True)

 def loadData(self,fileJSON):
    try:
      with open(fileJSON, 'r') as f:
         data = json.load(f)
    except FileNotFoundError:
      logging.error("FileNotFoundError",exc_info = True)
      exit()
    except json.JSONDecodeError:
      logging.error("JSONDecodeError",exc_info = True)
      exit()
    cursor = self.conn.cursor()
    tableName = os.path.basename(fileJSON)
    tableNameShort = os.path.splitext(os.path.basename(fileJSON))[0]
    if tableName == "rooms.json":
      try:
         cursor.execute(f" CREATE TABLE IF NOT EXISTS Rooms  ( 	 id INTEGER PRIMARY KEY, 	 name VARCHAR(15)  )")
         for item in data:
            cursor.execute(f"INSERT INTO {tableNameShort} VALUES (%s,%s)",(item["id"],item["name"]))
         logging.info('Data to rooms loaded successfully!')

      except psycopg2.errors.UniqueViolation:
        logging.warning( "Table rooms has been already filled")

    elif tableName == "students.json":
      try:
         cursor.execute(f"CREATE TABLE IF NOT EXISTS Students  ( 	 birthday DATE, 	 id INTEGER PRIMARY KEY, 	 name VARCHAR(30), 	 room INTEGER, 	 sex VARCHAR(1), 	 FOREIGN KEY (id) REFERENCES Students(id)  )")
         for item in data:
            cursor.execute(f"INSERT INTO {tableNameShort} VALUES (%s,%s,%s,%s,%s)",(item["birthday"],item["id"],item["name"],item["room"],item["sex"]))
         logging.info('Data to students loaded successfully!')

      except psycopg2.errors.UniqueViolation:
        logging.warning( "Table students has been already filled")
        
    else:
      logging.error('incorrect data')
      exit()

    self.conn.commit()
   
 def queryProccessing(self,query,format):
   cursor = self.conn.cursor()
   try:
      with open(query) as q:
         q_text = q.read()
      logging.info("queries recived successfully")
   except FileNotFoundError:
      logging.error("FileNotFoundError",exc_info = True)
      exit(1) 
   splitted = q.name.split(".")
   cursor.execute(q_text)
   result = cursor.fetchall()
   column_count = len(cursor.description)
   column_names = [desc[0] for desc in cursor.description]
   format = outputFormat[format]
   match format:
     case outputFormat.JSON:
       with open(splitted[0] + "_result.json",'w') as rf:
        json.dump(result,rf)
        logging.info('query finished(JSON result)')
     case outputFormat.XML:
       root = ET.Element("data")
       for row in result:
         item = ET.SubElement(root,"item")
         i = 0
         while i < column_count:
           ET.SubElement(item,column_names[i]).text = str(row[i])
           i += 1
       tree = ET.ElementTree(root)
       tree.write(splitted[0] + "_result.xml")
       logging.info('query finished(XML result)')

base = Database()
base.connectDatabase()
base.loadData(os.getenv('FILES_ROOMS'))
base.loadData(os.getenv('FILES_STUDENTS'))
base.queryProccessing(os.getenv('QUERY_QUERY_FILE'),os.getenv('QUERY_FORMAT'))
