# pytest -sv test_Assignment_17_pytestMethods.py
def sample():
    print("sample 1 function")

sample()

class Demo:
    def sample1(self):
        print("sample 1 method")
d= Demo()
d.sample1()

def test_tc1():
    print("testcase1 function")

def test_tc2():
    print("testcase2 function")

def TC1_test():
    print("3rd test")

class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def test_m2(self):
        print("m2 testcase2")

class Testsmile:
    def m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")


class TestDemo:
    def __init__(self):
        print("im a constructor")
    def test_m1(self):
        print("m1 testcase")