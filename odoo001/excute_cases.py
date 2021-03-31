# -*- coding:utf8 -*-

#测试报告生成
import HTMLTestRunner
import os, time, datetime, unittest

class TestRunner(object):
    '''Run test'''
    def __init__(self,cases="C:/Users/Administrator/PycharmProjects/odoo001",title=u"测试报告",description=u"用例执行情况"):
        self.cases = cases
        self.title = title
        self.des = description
    def run(self):
        for filename in os.listdir(self.cases):
            if filename == 'test_report':
                break
        else:
            os.mkdir(self.cases+'/test_report/')
        ret_path = "./test_report/" + '/result.html'
        fp = open(ret_path,'wb')  # html报告文件路径
        suite = unittest.TestLoader().discover("./testcases",pattern='pagecase_*.py',top_level_dir=None)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况")
        runner.run(suite)
        fp.close()

if __name__=="__main__":
    # 将结果写入
    print('=====AutoTest Start======')
    now_time = datetime.datetime.strptime(str(datetime.datetime.now()).split(".")[0], "%Y-%m-%d %H:%M:%S")  # 当前时间
    print(now_time)
    test = TestRunner()
    test.run()
    print('=====AutoTest Over======')
