"""
登录成功 http://ihrm-java.itheima.net/api/sys/login	POST	json
{"username": "13800000001", "password": "123456"}
"""
# 登录
# 1、导入包
import requests
import json
from utils.RequestsUtil import requests_get
from utils.RequestsUtil import requests_post
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
import pytest
from utils.AssertUtil import AssertUtil
from common.Base import init_db


# 2、定义登录方法
def test_login():
    # 3、定义测试数据
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/sys/login"
    # url = "http://ihrm-java.itheima.net/api/sys/login"
    data = {"mobile": "13800000002", "password": "888itcast.CN764%..."}
    headers = {"Content-Type": "application/json"}
    # 4、发送POST请求
    # r = requests.post(url, json=data, headers=headers)
    # r = requests_post(url, json=data, headers=headers)
    request = Request()
    r = request.post(url, json=data, headers=headers)
    # 5、输出结果
    # print(r.json())
    print(r)
    # 验证
    # 返回状态码
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    # 返回body
    # body = json.dumps(r["body"])
    # assert '"success": true,"data": "9829dd98-6dcc-41e1-901d-4e434cde36d6"' in body
    body = r["body"]
    AssertUtil().assert_in_body(body, '"success": true')
    # 1、初始化数据库对象
    conn = init_db("db_1")
    # 2、查询结果
    res_db = conn.fetchone("select id,name from users where name='cs14@cs14.com'")
    print("数据库查询结果", res_db)
    # 3、验证
    assert res_db[0] == '4Gm1gM6YTYU'


def getSecurity():
    # 定义测试数据
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/company/department"
    # url = "http://ihrm-java.itheima.net/api/company/department"
    token = "7c49522b-e17b-42d8-990d-5ffa687c918d"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token}
    # 发送get请求
    # r = requests.get(url, headers=headers)
    # r = requests_get(url, headers=headers)
    request = Request()
    r = request.get(url, headers=headers)
    # 输出结果
    # print(r.json())
    print(r)


def checkPpo():
    ppo_id = "PPO230809F000090"
    url = "https://rockbang.com.cn/api/sss/auth/technical_support/syncPOStatus/" + ppo_id
    cookie = {
        "sid": "b782212e-47fc-49f3-b278-bd8069f1e4c0"
    }
    # BladeAuth = "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ1c2VyX2VudGVycHJpc2VfaWQiOlsiRW50ZXJwcmlzZTEiXSwic2ltdWxhdGVkX2xvZ2luX2ZsYWciOjAsInVzZXJfbmFtZSI6ImFkbWlu77yI6LaF57qn566h55CG6LSm5Y-377yJIiwidG9rZW5fdHlwZSI6ImFjY2Vzc190b2tlbiIsImN1cnJlbnRfZW50ZXJwcmlzZSI6IkVudGVycHJpc2UxIiwidXNlcl9pZCI6IlNzc1VzZXIwMDAxIiwicm9sZV9pZCI6W10sImRlcHRfaWQiOlsiNEgyUThmNGhyalkiLCJkZXBhcnRtZW50MSIsIjRCR1djM1B4b29DIiwiNG41YVVvUThZbjciLCI0R1NIRlRYN2VQNyIsIjRCVXVLc1pYWXNtIl0sImFjY291bnQiOiJhZG1pbu-8iOi2hee6p-euoeeQhui0puWPt--8iSIsImVtYWlsIjoiYWRtaW5Ac3NzLmNvbSIsImNsaWVudF9pZCI6InN3b3JkIiwiZXhwIjoxNjkyMDE5MDg5LCJuYmYiOjE2OTE2NTkwODl9.ETQulSiyZU3OG9PjV16MzPiU3YY4CBpuN3b6a4zFb_517KO2MsyNMvNiXzT3c16kD3HI9_ApSotKIowjgm_pGA"
    # ClientInfo = "c3dvcmQ6c3dvcmRfc2VjcmV0"
    # TenantId = 000000
    # headers = { "Authorization": "Basic" + " " + ClientInfo, "Blade-Auth": "BladeAuth", "Tenant-Id": "Tenant"}
    request = Request()
    r = requests.post(url, cookies=cookie)
    print(r)


def tLogin():
    url = "https://bo-cas.rockbang.com.cn/api/go-cas/anon/login?service=https://rockbang.com.cn/usercenter/cas/callback"
    data = {"username": "admin@sss.com", "password": "Sss@123", "type": "email", "country_code": 86}
    cookies = {
        "sid": "b782212e-47fc-49f3-b278-bd8069f1e4c0"
    }
    r = requests.post(url, json=data, cookies=cookies)
    print(r.json())


# 【项目创建】执行单是否创建成功

def isCreate():
    url = "https://rockbang.com.cn/api/sss/auth/task_hub/ticket/list"
    data = {"fuzzySearchableText": "cs14 mm 0809-1"}
    cookies = {
        "sid": "b782212e-47fc-49f3-b278-bd8069f1e4c0"
    }
    r = requests.post(url, json=data, cookies=cookies)
    print(r.json())


if __name__ == '__main__':
    # login()
    # getSecurity()
    pytest.main(["-s"])
