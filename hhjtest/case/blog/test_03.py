import unittest
from time import sleep


class test_01(unittest.TestCase):
    def setUp(self):
        print("start!")

    def test01(self):
        print("执行测试用例test_03_01")

    def test02(self):
        print("执行测试用例test_03_02")

    def test03(self):
        print("执行测试用例test_03_03")

    def tearDown(self):
        print("end")

if __name__=="__main__":
    unittest.main()