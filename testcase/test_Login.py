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
import time
import allure


class TestProjectModel:
    # 2、定义登录方法
    @allure.title("测试登录")
    @allure.description("执行测试登录的结果是test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test1_login(self):
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

    # def getSecurity(self):
    #     # 定义测试数据
    #     conf_y = ConfigYaml()
    #     url_path = conf_y.get_conf_url()
    #     url = url_path + "/company/department"
    #     # url = "http://ihrm-java.itheima.net/api/company/department"
    #     token = "7c49522b-e17b-42d8-990d-5ffa687c918d"
    #     headers = {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token}
    #     # 发送get请求
    #     # r = requests.get(url, headers=headers)
    #     # r = requests_get(url, headers=headers)
    #     request = Request()
    #     r = request.get(url, headers=headers)
    #     # 输出结果
    #     # print(r.json())
    #     print(r)
    #

    # def test_login(self):
    #     url = "https://rockbang.com.cn/rdxapi/blade-auth/cas/admin/token?grant_type=cas_admin"
    #     data = {"userId": "SssUser0001", "userName": "admin（超级管理账号）"}
    #     cookie = {
    #         "sid": "f4ae236e-9481-487f-bacd-f49b562a833b"
    #     }
    #     request = Request()
    #     r = request.post(url, json=data, cookies=cookie)
    #     print(r)

    # 创建MM项目
    @pytest.fixture(scope="module")
    def test_createmmpj(self):
        timestamp = int(time.time())
        dt_object = time.localtime(timestamp)
        formatted_time = time.strftime("%Y-%m-%d", dt_object)
        formatted_time1 = time.strftime("%m%d%H%M%S", dt_object)
        print("时间戳转换为日期时间对象：", formatted_time)
        url = "https://rockbang.com.cn/api/sss/auth/project_hub/create_project"
        data = {
            "operatorId": "",
            "projectName": "cs12 test" + " " + formatted_time1,
            "ownerId": "4GcrWZrTeFN",
            "initiationTime": formatted_time + "T16:00:00.000Z",
            "managerId": "SssUser0001"
        }

        cookie = {
            "sid": "98134489-cca1-48b8-ab6c-4a07362a0349"
        }
        request = Request()
        r = request.post(url, json=data, cookies=cookie)
        print(r)
        r_data = r.json()

        project_id = r_data['body']['content']['data']
        print(project_id)
        yield project_id
        # 验证
        # 返回状态码
        # AssertUtil().assert_code(pj_r.status_code, 200)
        # return pj_r

    def test_selectpj(self, project_id):
        project_id = project_id
        url = "https://rockbang.com.cn/api/sss/auth/project_hub/project_details/{project_id}"
        cookie = {
            "sid": "98134489-cca1-48b8-ab6c-4a07362a0349"
        }
        request = Request()
        r = request.get(url=url, cookies=cookie)
        print(r)

    # 【项目创建】执行单是否创建成功

    def test1_iscreate(self):
        url = "https://rockbang.com.cn/api/sss/auth/task_hub/ticket/list"
        data = {"fuzzySearchableText": "cs12 test 0921-4"}
        headers = {"Content-Type": "application/json"}
        cookies = {
            "sid": "41fb8df9-d426-4eda-bd2f-b2d586535137"
        }
        r = requests.post(url, json=data, cookies=cookies, headers=headers)
        print(r.json())
        # 验证
        # 返回状态码
        AssertUtil().assert_code(r.status_code, 200)


if __name__ == '__main__':
    # login()
    # getSecurity()
    pytest.main(["-s", "test_Login.py"])
