import os
from utils.YamlUtil import YamlReader

# 1、获取项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)
# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"
# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + "conff.yml"


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


# 2、读取配置文件
# 创建类
class ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

    # 定义方法获取需要信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]


if __name__ == '__main__':
    conf_read = ConfigYaml()
    print(conf_read.get_conf_url())
