# 1、导包
import psycopg2
from psycopg2 import extras
from utils.LogUtil import my_log


class Postgresql:
    # 2.初始化数据，连接数据库，光标对象
    def __init__(self, host, database, user, password, port=3306):
        self.log = my_log()
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        # self.cursor = self.conn.cursor()
        # 创建数据字典光标对象
        self.cursor = self.conn.cursor(cursor_factory=extras.DictCursor)

        # 3、创建查询、执行方法
    def fetchone(self, sql):
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        """
        执行
        :param sql:
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Postgresql 执行失败")
            self.log.error(ex)
            return False
        return True

    # 4、关闭对象
    def __del__(self):
        # 关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接对象
        if self.conn is not None:
            self.conn.close()


if __name__ == "__main__":
    postgresql = Postgresql("rockbang.com.cn",
                            "sss",
                            "sss_u",
                            "S3*Rb!358",
                            5432
                            )
    res = postgresql.fetchone("SELECT id,name FROM users")
    print(res)

"""
# 1、导入pymysql包
import psycopg2

# 2、链接database
try:
    conn = psycopg2.connect(
        host="rockbang.com.cn",
        database="sss",
        user="sss_u",
        password="S3*Rb!358",
        charset="utf8",
        port=5432
    )
    print("连接成功")

    # 3、获取执行sql的光标对象
    cursor = conn.cursor()

    # 4、执行sql
    cursor.execute("SELECT id,name FROM users")
    # 获取查询结果
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("连接失败:", error)

finally:
    # 5、关闭游标和数据库连接
    if cursor:
        cursor.close()
    if conn:
        conn.close()

        print("连接已关闭")
"""
