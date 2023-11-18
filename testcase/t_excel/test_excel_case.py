from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
import json
import pytest
from common import Base

# 参数化接口请求
# 1、初始化信息
# 1).初始化测试用例文件
case_file = os.path.join("../../data/" + ConfigYaml().get_excel_file())
# 2).测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# 3).获取运行测试用例列表
data_init = Data(case_file, sheet_name)
run_list = data_init.get_run_data()
# print(run_list)
# 4).日志
log = my_log()

# 初始化datacofig
data_key = ExcelConfig.DataConfig


# 2、测试用例方法，参数化运行
# 一个用例的执行
class TestExcel:
    # 1、增加pytest
    # 2、修改方法参数
    # 3、重构函数内容
    # 4、pytest.main

    def run_api(self, url, method, params=None, header=None, cookie=None):
        """
        发送请求api
        :return:
        """
        # 2).接口请求
        request = Request()
        # params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        # method post/get
        if str(method).lower() == "get":
            # 增加headers
            res = request.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            # 增加headers
            res = request.post(url, json=params, headers=header, cookies=cookie)
        else:
            log.error("错误请求method：%s" % method)
        return res

    def run_pre(self, pre_case):
        # 初始化数据
        pass
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]

        # 判断headers是否存在，json转义（因为excel是字符形的）
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        header = Base.json_parse(headers)
        # 增加cookies
        # if cookies:
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies
        cookie = Base.json_parse(cookies)
        self.run_api(url, method, params, header)

    # 1).初始化信息，url，data
    @pytest.mark.parametrize("case", run_list)
    def test_run(self, case):
        # data_key = ExcelConfig.DataConfig
        # run_list第1个用例，用例，key获取values
        url = ConfigYaml().get_conf_url() + case[data_key.url]+case[data_key.params]
        print(url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]

        # 判断headers是否存在，json转义（因为excel是字符形的）
        if headers:
            header = json.loads(headers)
        else:
            header = headers
        # 增加cookies
        if cookies:
            cookie = json.loads(cookies)
        else:
            cookie = cookies
        # 1、验证前置条件
        if pre_exec:
            pass
            # 2、找到前置用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息为:%s" % pre_case)
            self.run_pre(pre_case)
        # 2).接口请求
        request = Request()
        # params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        # method post/get
        if str(method).lower() == "get":
            # 增加headers
            res = request.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            # 增加headers
            res = request.post(url, json=params, headers=header, cookies=cookie)
        else:
            log.error("错误请求method：%s" % method)
        print(res)


if __name__ == '__main__':
    pytest.main(["-s", "test_excel_case.py"])
