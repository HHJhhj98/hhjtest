import unittest
from time import sleep

from selenium import webdriver


class test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    def test01(self):
        """错误用例截图"""
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('xxxxx').send_keys(u'百度一下')
        self.driver.find_element_by_id('su').click()
        self.assertTrue(True)


    def test02(self):
        print("执行测试用例test_02_02")

    @unittest.skip('跳过')
    def test03(self):
        print("执行测试用例test_02_03")

    def tearDown(self):
        print("end")

if __name__=="__main__":
    unittest.main()