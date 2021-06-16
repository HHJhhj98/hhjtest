import HTMLTestRunner_cn
import unittest
import os
from emailUtil import emailUtil
#单线程执行测试用例
#用例存放路径
path=os.path.dirname(os.path.realpath(__file__))
print(path)
case_path=os.path.join(path,'case')
#报告存放路径
report_path=os.path.join(path,'report')


def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(title="可以装逼的测试报告", description="测试结果", stream=fp, verbosity=2, retry=1,save_last_try=True)
    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()
    #receiver = ["3281502659@qq.com"]
    #emial=emailUtil()
    #emial.send_mail("smtp.qq.com",465,"2393022053@qq.com","wnbikhqoteyqebja",receiver,report_abspath,"这个我的主题",u"test_report.html")