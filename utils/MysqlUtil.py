
# 1、导入pymysql包
import pymysql
# 2、链接database
conn = pymysql.connect(
    host = "rockbang.com.cn",
    user = "sss_u",
    password= "S3*Rb!358",
    database= "sss",
    charset = "utf8",
    port =5432
)
# 3、获取执行sql的光标对象
cursor = conn.cursor()
# 4、执行sql
sql = "select id,name from users"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
# 5、关闭对象
cursor.close()
conn.close()




