
from httprunner.api import HttpRunner

runner = HttpRunner(failfast=False)
# coding=utf-8

"""
@作者: Angst
@邮箱: zhouqing@yunjiglobal.com
@开发工具: PyCharm
@创建时间: 2019/12/9 15:23
"""

from httprunner.api import HttpRunner

runner = HttpRunner(failfast=False, log_level='debug')
# runner.run_path('testcases')

# # dot_env_path
# runner.run("testcases", dot_env_path="docker.env")

#
# # mapping
# # override_mapping = {
# #     "merchantCode": "SX537607"
# # }

# #
# runner.run("docs/data/demo-quickstart-2.yml", mapping=override_mapping)

# get result summary
# summary = runner.summary


def runTestCase(obj, dot=None, mapping=None):
    return runner.run(obj, dot_env_path=dot, mapping=mapping)


if __name__ == '__main__':
    print(runTestCase(r'testcases\分账平台\test_subAccountQuery.yml'))
