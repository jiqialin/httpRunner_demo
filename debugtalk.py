
import pymysql
import time
import demjson


def getBufferedReader(file_path):
    return open(file_path, 'rb')


def sleep(n_secs):
    time.sleep(n_secs)


def hook_print(msg):
    print(msg)


def teardown_hook_sleep_N_secs(response):
    """
        Do something before the test case .
          tips:  sleep n seconds after request
    :param response: response objects
    :return:
    """
    if response.status_code == 200:
        print('sleep 1 sec')
        sleep(1)
    else:
        print('The state is not expected .')


def setup_hook_prepare_kwargs(request):
    """
        Do something before the test case .
    :param request:
    :return:
    """
    print('Determine whether the data format needs to be transformed before request.')
    if request["method"] == "POST":
        content_type = request.get("headers", {}).get("content-type")
        if content_type and "data" in request:
            if content_type.startswith("application/json") and isinstance(request["data"], (dict, list)):
                request["data"] = demjson.encode(request["data"])
            elif isinstance(request["data"], str):
                request["data"] = request["data"].encode('utf-8')


def setup_hook_http_ntlm_auth(request):
    if "httpntlmauth" in request:
        from requests_ntlm import HttpNtlmAuth
        auth_account = request.pop("httpntlmauth")
        request["auth"] = HttpNtlmAuth(
            auth_account["username"], auth_account["password"])


def searchSqlSyntax(sql_syntax):
    """ DQL Example
        :param sql_syntax: select * from `db_name`.`table_name` where field condition values.
        :return:
    """
    db = pymysql.connect(host='127.0.0.1', port=3306,
                         user='root', passwd='123456', charset='utf8')
    cur = db.cursor()  # cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cur.execute(sql_syntax)
        result = cur.fetchall()[0][0]
    except Exception as e:
        return f'execute sql exception: {e}'
    else:
        return result
    finally:

        db.close()


def alterSqlSyntax(sql_syntax):
    """  DDL、DML operation example
        :param sql_syntax: alter table `db_name`.`table_name` where field condition values.
        :return:
    """
    db = pymysql.connect(host='127.0.0.1', port=3306,
                         user='root', passwd='123456', charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql_syntax)
        db.commit()
    except Exception as e:
        db.rollback()
        return f'execute sql exception: {e}'
    finally:
        db.close()


if __name__ == '__main__':
    r = searchSqlSyntax('SELECT * FROM `my_django`.`case_info` LIMIT 0, 1000')
    print(r)

