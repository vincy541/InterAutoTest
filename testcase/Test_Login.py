"""
登录成功 http://ihrm-java.itheima.net/api/sys/login	POST	json
{"username": "13800000001", "password": "123456"}
"""
# 登录
# 1、导入包
import requests
from utils.RequestsUtil import requests_get
from utils.RequestsUtil import requests_post
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml


# 2、定义登录方法
def login():
    # 3、定义测试数据
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path+"/sys/login"
    # url = "http://ihrm-java.itheima.net/api/sys/login"
    data = {"mobile": "13800000002", "password": "123456"}
    headers = {"Content-Type": "application/json"}
    # 4、发送POST请求
    # r = requests.post(url, json=data, headers=headers)
    # r = requests_post(url, json=data, headers=headers)
    request = Request()
    r = request.post(url, json=data, headers=headers)
    # 5、输出结果
    # print(r.json())
    print(r)


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


if __name__ == '__main__':
    login()
    # getSecurity()
