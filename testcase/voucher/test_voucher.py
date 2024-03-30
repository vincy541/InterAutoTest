from common.Base import init_db
import pytest
from utils.RequestsUtil import Request
from utils.YamlUtil import YamlReader
from common import common
from utils.AssertUtil import AssertUtil

base_url = "https://rockbang.com.cn/api/sss/auth"


def test_complete_booking():
    # 1、初始化数据库对象
    conn = init_db("db_1")
    # 2、查询结果
    res_db = conn.fetchone(
        "select * from shipping_voucher where shipping_document_id  ='52XSeTmQLUC' and type='Booking'")
    print("数据库查询结果，订舱委托id：", res_db['id'])

    # 一、完成「订舱委托」任务
    booking_url = base_url + "/shipping_written_material/booking/" + res_db['id'] + "?provide_from_order_hub=true"
    # 1.读取yaml文件
    filling_data = YamlReader("../../data/filling_booking.yml").data()
    # 获取sid
    cookie = {
        "sid": common.get_sid()
    }
    request = Request()
    r = request.post(booking_url, json=filling_data, cookies=cookie)
    print(r)
    # AssertUtil().assert_code(r["code"], 200)

    # 判断「订舱委托」任务是否已完成
    # 1.获取「订舱」执行单id，传入货运单ID
    select_id = {
        "groupId": "52XSeTmQLUC"
    }
    ticket_details = common.ticket_details(select_id)
    # print(ticket_details.json())
    booking_ticket_type = '0604001'
    # 遍历结果
    for voucher_ticket in ticket_details.json()['content']['ticketDetails']:
        if voucher_ticket['ticket']['type'] == booking_ticket_type:
            # 找到匹配的执行单，获取执行单id
            booking_ticket_id = voucher_ticket['ticket']['id']
            # print("订舱委托执行单id：", booking_ticket_id)

            # 找到当前执行单下的「订舱委托」任务，校验任务为已完成
            select_id = {
                "ticketIds": [f"{booking_ticket_id}"]
            }
            task_details = common.task_detail(select_id)
            # 订舱委托任务type=0604001001
            booking_task_type = '0604001001'
            for ticket_details in task_details.json()['content']['taskDetails']:
                if ticket_details['task']['type'] == booking_task_type:
                    # 匹配「订舱委托」任务，获取任务状态
                    booking_task_status = ticket_details['task']['status']
                    print("「订舱信息」任务状态为：", booking_task_status)
                    # assert booking_task_status == 6
                    if AssertUtil.assert_body(booking_task_status, booking_task_status, 6):
                        print("成功完成【订舱委托】任务")
                        break
                    else:
                        # 如果没有找到匹配的任务
                        print("「订舱委托」任务，未完成")

            # booking发送货代任务type=0604001002
            booking_send_task_type = '0604001002'
            for ticket_details in task_details.json()['content']['taskDetails']:
                if ticket_details['task']['type'] == booking_send_task_type:
                    # 匹配「booking发送货代」任务，获取任务uid和id
                    booking_send_task_id = ticket_details['task']['id']
                    booking_send_task_uid = ticket_details['task']['uid']
                    print("「booking发送货代」任务id：", booking_send_task_id)
                    print("「booking发送货代」任务uid：", booking_send_task_uid)

                    # 二、完成「booking发送货代」任务
                    booking_send_url = f"{base_url}/order_hub/save_task_content"
                    booking_send_data = {
                        "data": "{}",
                        "taskUid": booking_send_task_uid,
                        "taskId": booking_send_task_id
                    }
                    request = Request()
                    r = request.post(booking_send_url, json=booking_send_data, cookies=cookie)
                    # print(r)
                    # 验证「booking发送货代」任务完成
                    booking_send_task_status = ticket_details['task']['status']
                    print("「booking发送货代」任务状态为：", booking_send_task_status)
                    # assert booking_send_task_status == 6
                    if AssertUtil.assert_body(booking_send_task_status, booking_send_task_status, 6):
                        print("成功完成「booking发送货代」任务")
                    else:
                        # 如果没有找到匹配的任务
                        print("「booking发送货代」任务，未完成")

    # 三、完成「货代放舱/SO上传」任务
    # 查询数据库，获取货代放舱任务的id
    db_forwarder_id = conn.fetchone(
        "select * from shipping_voucher where shipping_document_id  ='52XSeTmQLUC' and type='ShippingOrder'")
    print("数据库查询结果，货代放舱id：", db_forwarder_id['id'])

    # 获取url
    forwarder_url = base_url + "/shipping_written_material/forwarder/" + db_forwarder_id['id'] + "?provide_from_order_hub=true"
    # 获取请求参数
    forwarder_data = YamlReader("../../data/voucher/filling_forwarder.yml").data()
    request = Request()
    r = request.post(forwarder_url, json=forwarder_data, cookies=cookie)
    print(r)
    AssertUtil().assert_code(r["code"], 200)
    # 判断货代放仓任务是否完成
    # 货代放仓任务type = 0604001003
    # forwarder_task_type = '0604001003'
    # 传入请求参数
    select_id = {
        "groupId": "52XSeTmQLUC"
    }
    ticket_type = '0604001'
    task_type = '0604001003'
    r = common.task_status(select_id, ticket_type, task_type)
    if r == 6:
        print("「货代放仓」任务正常完成")

    # 四、完成「SO发送工厂」任务
    # 1.完成任务
    so_url = f"{base_url}/order_hub/save_task_content"
    so_data = {
        "data": "{}",
        "taskUid": "52XSCCc2Cqb",
        "taskId": "Bb1TtD8ZKW"
    }
    r = request.post(so_url, json=so_data, cookies=cookie)


