import time
import pytest


def test_gettime():
    timestamp = int(time.time())
    dt_object = time.localtime(timestamp)
    print("时间戳转换为日期时间对象：", dt_object)
    # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", dt_object)
    # print("格式化后的时间字符串：", formatted_time)


if __name__ == '__main__':
    pytest.main(["-s"])
