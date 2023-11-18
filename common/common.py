import requests


def get_sid():
    return "667601a0-286f-4a83-b59f-40dcda4d1d86"


def create_project(projectdata, cookie):
    url = 'https://rockbang.com.cn/api/sss/auth/project_hub/create_project'
    r = requests.post(url=url, json=projectdata, cookies=cookie)
    return r


def project_detail(pid, cookie):
    url = 'https://rockbang.com.cn/api/sss/auth/project_hub/project_details/' + pid
    return requests.get(url=url, cookies=cookie)
