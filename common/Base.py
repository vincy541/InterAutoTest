from config.Conf import ConfigYaml
from utils.PostgresqlUtil import Postgresql
import json


# 1、定义init_db
def init_db(db_alias):
    # 2、初始数据库信息，通过配置
    db_info = ConfigYaml().get_db_config_info(db_alias)
    host = db_info["db_host"]
    database = db_info["db_database"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    port = int(db_info["db_port"])
    # 3、初始化postgresql对象
    conn = Postgresql(host, database, user, password, port)
    print(conn)
    return conn


def json_parse(data):
    """
    格式化字符，转换json
    :param data:
    :return:
    """
    # if headers:
    #     header = json.loads(headers)
    # else:
    #     header = headers
    return json.load(data) if data else data


if __name__ == '__main__':
    init_db("db_1")
