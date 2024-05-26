import json
import unittest
import Task_1
class TestTask_1(unittest.TestCase):

    def setUp(self):
        self.testBase = Task_1.Database('TEST_DATABASE_NAME','DATABASE_USER','DATABASE_PASSWORD','TEST_DATADASE_HOST','DATABASE_PORT')


    def test_connect(self):
        self.testBase.connectDatabase()
        self.assertIsNotNone(self.testBase.conn)

    def test_query_check_xml(self):
        self.testBase.connectDatabase()
        self.testBase.loadData(r'FILES_ROOMS')
        self.testBase.loadData(r'FILES_STUDENTS')
        self.testBase.queryProccessing(r'QUERY_QUERY_FILE',"JSON")
        with open(r'QUERY_RESULT','r') as resF:
            data1 = json.load(resF)
        with open(r'QUERY_EXPECTED_RESULT','r') as expRes:
            data2 = json.load(expRes)
        self.assertEqual(data1,data2)

    

if __name__ == '__main__':
    unittest.main()