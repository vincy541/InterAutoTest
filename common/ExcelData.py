from utils.ExcelUtil import ExcelReader
from config import Conf
from common.ExcelConfig import DataConfig
from config.Conf import ConfigYaml
import os


class Data:
    def __init__(self, testcase_file, sheet_name):
        # 1、使用excel工具类，获取结果list
        # self.reader = ExcelReader(Conf.get_excel_data_file(),"登录")
        self.reader = ExcelReader(testcase_file, sheet_name)
        # print(reader.data())

    # 2、从excel中判断用例是否要运行
    def get_run_data(self):
        """
        根据是否运行列==y，获取执行测试用例
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                # print(line)
                # 3、保存要执行结果，放到新的列表
                run_list.append(line)
        # print(run_list)
        return run_list

    def get_case_list(self):
        """
        获取全部用例
        :return:
        """
        # run_list = list()
        # for line in self.reader.data():
        #     run_list.append(line)
        # 加列表推广
        run_list = [line for line in self.reader.data()]
        return run_list

    def get_case_pre(self, pre):
        # 获取全部测试用例
        # list判断，执行，获取
        """
        根据前置条件，从全部测试用例中取到对应的用例
        :param pre:
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None


if __name__ == '__main__':
    case_file = os.path.join("../data/" + ConfigYaml().get_excel_file())
    reader = Data(case_file, ConfigYaml().get_excel_sheet())
    print(reader.get_run_data())
    print(reader.get_case_pre("存在项目"))
