import pytest

"""
1、定义类
2、创建测试方法test开头
3、创建setup、teardown
4、运行查看结果
"""


# 1、定义类
class TestFunc:
    # 3、创建setup，teardown
    def setup(self):
        print("---setp---")

    def teardown(self):
        print("---teardown---")

    # 2、创建测试方法test开头
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")


if __name__ == "__main__":
    pytest.main(["-s", "pytest_func.py"])
