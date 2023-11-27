import pytest
import requests
from utils.RequestsUtil import Request
import time
from common import common
from utils.YamlUtil import YamlReader
from utils.AssertUtil import AssertUtil

base_url = "https://rockbang.com.cn/api/sss/auth"  # 替换为实际的API基础URL


# def access_sid():
#     # 假设在这里获取访问令牌的方法，例如登录并返回令牌
#     return "136c7976-eb78-4334-b2c9-bc5d54919572"  # 替换为实际的访问令牌


def test_create_project():
    # 创建项目接口请求
    # create_project_url = f"{base_url}/project_hub/create_project"
    timestamp = int(time.time())
    dt_object = time.localtime(timestamp)
    formatted_time = time.strftime("%Y-%m-%d", dt_object)
    formatted_time1 = time.strftime("%m%d%H%M%S", dt_object)
    print("时间戳转换为日期时间对象：", formatted_time)
    # url = "https://rockbang.com.cn/api/sss/auth/project_hub/create_project"
    create_project_data = {
        "operatorId": "",
        "projectName": "cs12 api" + " " + formatted_time1,
        "ownerId": "4GcrWZrTeFN",
        "initiationTime": formatted_time + "T16:00:00.000Z",
        "managerId": "SssUser0001"
    }

    cookie = {
        "sid": common.get_sid()
    }
    # request = Request()
    # response = request.post(create_project_url, json=create_project_data, cookies=cookie)
    r = common.create_project(create_project_data, cookie)
    print(r.json())
    pid = r.json()['content']['data']
    print("项目id为：", pid)
    r_detail = common.project_detail(pid, cookie)
    print(r_detail.json())
    # assert response.status_code == 201, "Failed to create project"

    # 提取项目ID
    # project_id = response
    # print(response)
    # assert project_id is not None, "Project ID not found in response"

    # yield project_id  # 返回项目ID作为fixture的值

    # 在测试完成后，可以在这里添加清理操作，例如删除测试项目


# 完成「项目信息」任务
def test_filling_project():
    filling_data = YamlReader("../data/filling_project.yml").data()
    # print(filling_data)
    filling_project_url = f"{base_url}/project_hub/filling_project"
    cookie = {
        "sid": common.get_sid()
    }
    request = Request()
    response = request.post(filling_project_url, json=filling_data, cookies=cookie)
    print(response)
    # 判断「项目信息」任务是否已完成
    # 1.查询任务详情
    select_data = {"groupId": "MPJ231118000011"}
    r = common.task_detail(select_data, cookie)
    # print(r.json()['content']['taskDetails'][1]['task']['type'])
    task_type = '0101001001'

    # 2.遍历结果，查找符合条件的任务
    for task_data in r.json()['content']['taskDetails']:
        if task_data['task']['type'] == task_type:
            # 找到匹配的任务，获取任务状态
            task_status = task_data['task']['status']
            print("项目信息任务状态为：", task_status)
            # assert task_status == 6
            if AssertUtil.assert_body(task_status, task_status, 6):
                print("成功完成【项目信息】任务")
            break
    else:
        # 如果没有找到匹配的任务
        print("没有找到项目信息任务")

def test_update_yaml():
