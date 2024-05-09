import json
import unittest
import Task_1
class TestTask_1(unittest.TestCase):

    def setUp(self):
        self.testBase = Task_1.Database("Test_Task_1","postgres","2005","127.0.0.1","5432")


    def test_connect(self):
        self.testBase.connectDatabase()
        self.assertIsNotNone(self.testBase.conn)

    def test_query_check_xml(self):
        self.testBase.connectDatabase()
        self.testBase.loadData(r"D:\Coding\Innowise internship\Projects\task_1\Data\testData\rooms.json")
        self.testBase.loadData(r"D:\Coding\Innowise internship\Projects\task_1\Data\testData\students.json")
        self.testBase.queryProccessing(r"D:\Coding\Innowise internship\Projects\task_1\Query_1.sql","JSON")
        with open(r"D:\Coding\Innowise internship\Projects\task_1\Query_1_result.json",'r') as resF:
            data1 = json.load(resF)
        with open(r"D:\Coding\Innowise internship\Projects\task_1\expected_result_q1.json",'r') as expRes:
            data2 = json.load(expRes)
        self.assertEqual(data1,data2)

    

if __name__ == '__main__':
    unittest.main()