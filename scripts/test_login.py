import pytest
# 使用pytest命令时，先导模块
# 在导模块时，避免有重名文件，否则会出现错误

class TestAB:

    def setup(self):
        print("1")
    def teardown(self):
        print("2")
    def setup_class(self):
        print("3")
    def teardown_class(self):
        print("4")

    # 用pytest在命令窗口运行此文件，自动识别去寻找test开头的类和函数
    def test_login1(self):
        assert 1
    # 断言 assert 1 成功        断言 assert 0 失败

    def test_login2(self):
        assert 1

    def test_login3(self):
        assert 1






# if __name__ == '__main__':
#     pytest.main(["-s","login.py"])
    # 让main函数使用pytest去检测执行 -s 指定 login.py文件
# 将其中的参数以列表的形式传给pytest.main中

# 在命令框窗口直接使用 pytest -s login.py  可直接运行文件中的函数

# 每个test函数运行前都会运行一个setup和teardown函数，有几个函数，就会运行多少次
# 每个test类运行前都会运行一个setup_class和teardown_class函数,只运行一次