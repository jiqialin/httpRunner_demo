
from httprunner.api import HttpRunner

runner = HttpRunner(failfast=False)
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


def runTestCase(obj, envs=None, dot=None, mapping=None):
    if envs == 'docker':
        dot = 'docker.env'
        runner.run(obj, dot_env_path=dot, mapping=mapping)
        return runner.summary
    elif envs is None:
        runner.run(obj, dot_env_path=dot, mapping=mapping)
        return runner.summary


if __name__ == '__main__':
    runTestCase('testcases')