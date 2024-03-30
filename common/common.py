import requests
from utils.AssertUtil import AssertUtil

base_url = "https://rockbang.com.cn/api/sss/auth"


def get_sid():
    return "e194411f-4d53-4c16-9839-65ef6750b765"


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


# 通过groupID查询任务详情，获取任务的状态

def task_status(groupId, ticket_type, task_type):
    ticket_url = f'{base_url}/task_hub/ticket/list'
    cookie = {
        "sid": get_sid()
    }
    ticket_detailss = requests.post(url=ticket_url, json=groupId, cookies=cookie)
    current_ticket_type = ticket_type
    print("当前执行单编码为：", current_ticket_type)
    # 遍历结果
    for voucher_ticket in ticket_detailss.json()['content']['ticketDetails']:
        if voucher_ticket['ticket']['type'] == current_ticket_type:
            # 找到匹配的执行单，获取执行单id
            current_ticket_id = voucher_ticket['ticket']['id']

            # 找到当前任务，校验任务为已完成
            select_id = {
                "ticketIds": [f"{current_ticket_id}"]
            }
            task_url = f'{base_url}/task_hub/task/list'
            task_details = requests.post(url=task_url, json=select_id, cookies=cookie)
            # 匹配当前完成的任务
            current_task_type = task_type
            for task in task_details.json()['content']['taskDetails']:
                if task['task']['type'] == current_task_type:
                    # 匹配当前任务，获取任务状态
                    current_task_status = task['task']['status']
                    print("当前任务状态为：", current_task_status)
                    return current_task_status
                    # # assert current_task_status == 6
                    # if AssertUtil.assert_body(current_task_status, current_task_status, 6):
                    #     print("成功完成当前任务")
                    #     break
                    # else:
                    #     # 如果没有找到匹配的任务
                    #     print("当前任务，未完成")

