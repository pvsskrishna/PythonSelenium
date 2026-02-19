import pytest
[pytest]
markers = ["smoke","m1","mark1",'p3','m2']

@pytest.mark.mark1
def test_case1():
    print("testCase1")

def test_case2():
    print("testCase2")

@pytest.mark.m2
def test_case3():
    print("testCase2")

@pytest.mark.smoke
def test_login():
    print("loginpage testcase")

@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")

@pytest.mark.smoke
def test_compose():
    print("compose testcase")

@pytest.mark.p3
def test_bin():
    print("bin testcase")