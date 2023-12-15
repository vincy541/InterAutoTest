import requests

base_url = "https://rockbang.com.cn/api/sss/auth"


def get_sid():
    return "5a92e452-7329-47f8-9805-c28e466db419"


# 创建项目
def create_project(projectdata):
    url = f'{base_url}/project_hub/create_project'
    cookie = {
        "sid": get_sid()
    }
    r = requests.post(url=url, json=projectdata, cookies=cookie)
    return r


# 获取项目详情
def project_detail(pid):
    url = f'{base_url}/project_hub/project_details/' + pid
    cookie = {
        "sid": get_sid()
    }
    return requests.get(url=url, cookies=cookie)


# 通过groupId查任务详情
def task_detail(conditions):
    url = f'{base_url}/task_hub/task/list'
    cookie = {
        "sid": get_sid()
    }
    return requests.post(url=url, json=conditions, cookies=cookie)


# 通过groupId查询执行单
def ticket_details(groupId):
    url = 'https://rockbang.com.cn/api/sss/auth/task_hub/ticket/list'
    cookie = {
        "sid": get_sid()
    }
    return requests.post(url=url, json=groupId, cookies=cookie)
