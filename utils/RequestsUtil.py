import requests


# 1、创建封装get方法
def requests_get(url, headers):
    # 2、发送requests get请求
    r = requests.get(url, headers=headers)
    # 3、获取结果内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
    # 5、字典返回
    return res


# post方法封装
# 1、创建post方法
def requests_post(url, json, headers):
    # 2、发送post请求
    r = requests.post(url, json=json, headers=headers)
    # 3、获取结果内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
    # 5、字典返回
    return res


# 重构
# 1、创建类
class Request:
    # 2、定义公共方法
    def requests_api(self, url, json=None, headers=None, method="get"):

        # 1.增加方法的参数，根据参数来验证方法get/post，方法请求
        if method == "get":
            # get请求
            r = requests.get(url, json=json, headers=headers)
        elif method == "post":
            # post请求
            r = requests.post(url, json=json, headers=headers)

        # 2.重复的内容复制进来
        # 获取结果内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 4、内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        # 5、字典返回
        return res

    # 3、重构get/post方法
    # get
    # 1、定义方法
    def get(self, url, **kwargs):
        # 2、定义参数
        # url,json,headers,cookies,method
        # 3、调用公共方法
        return self.requests_api(url, method="get", **kwargs)

    # post
    def post(self, url, **kwargs):
        # 2、定义参数
        # url,json,headers,cookies,method
        # 3、调用公共方法
        return self.requests_api(url, method="post", **kwargs)
