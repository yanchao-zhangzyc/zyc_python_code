import requests
import unittest
import json

class Test(unittest.TestCase):
    def setUp():
        self.url="http://wwww.baidu.com"
        self.pyload={"key1":"value1",
                "key2":"value"}
        print("测试开始")
    def tearDown():
        print("测试结束")
    def test_case1(self):
        r=requests.post(self.url,data=self.pyload)
        t=r.json()
        self.assertEqual(t['url'],self.url)
    def test_case2(self):
        r=requests.post(self.url,data=self.pyload)
        self.assertEqual(r.status_code,200)
if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(Test('test_case1'))
    suite.addTest(Test('test_case2'))
    runner=unittest.TextTestRunner
    runner.run(suite)