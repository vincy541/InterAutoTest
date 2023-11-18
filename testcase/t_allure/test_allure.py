import pytest
import allure


# 测试方法
@allure.title("测试用例标题1")
@allure.description("执行测试用例1的结果是test1")
@allure.severity(allure.severity_level.BLOCKER)
def test_1():
    print("test1")


@allure.title("测试用例标题2")
@allure.description("执行测试用例1的结果是test2")
@allure.severity(allure.severity_level.CRITICAL)
def test_2():
    print("test2")


@allure.title("测试用例标题3")
@allure.description("执行测试用例1的结果是test3")
def test_3():
    print("test3")


@pytest.mark.parametrize("case", ["case1", "case2"])
def test_4(case):
    print("case")
    allure.dynamic.title(case)


if __name__ == '__main__':
    pytest.main(["test_allure.py"])
