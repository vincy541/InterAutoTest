import requests


def get_sid():
    return "db6c1d57-0ec8-4103-8a2b-4e97252c4bb3"


# 创建项目
def create_project(projectdata, cookie):
    url = 'https://rockbang.com.cn/api/sss/auth/project_hub/create_project'
    r = requests.post(url=url, json=projectdata, cookies=cookie)
    return r


# 获取项目详情
def project_detail(pid, cookie):
    url = 'https://rockbang.com.cn/api/sss/auth/project_hub/project_details/' + pid
    return requests.get(url=url, cookies=cookie)


# 通过groupId查任务详情
def task_detail(conditions, cookie):
    url = 'https://rockbang.com.cn/api/sss/auth/task_hub/task/list'
    return requests.post(url=url, json=conditions, cookies=cookie)
