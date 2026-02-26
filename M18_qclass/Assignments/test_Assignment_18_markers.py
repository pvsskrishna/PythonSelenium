import pytest

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

@pytest.mark.smoke
@pytest.mark.p3
def test_trash():
    print("tash testcase")

@pytest.mark.smoke
def test_compose():
    print("compose testcase")

@pytest.mark.p3
def test_bin():
    print("bin testcase")


@pytest.mark.skip(reason = 'not important' )
def test_bin():
    print("Skip test case with reason")


@pytest.mark.xfail(reason='xfail checking 1')
def test_xfail1():
    print("xfail test 1")

brw = 'safari'
@pytest.mark.xfail(brw in ['chrome','IE','firefox'],reason = 'not implemented ')
def test_xfail2():
    print("xfail test 2")
@pytest.mark.xfail
def test_xfail3():
    print("xfail test 3")

@pytest.mark.xfail
def test_xfail4():
    print("xfail test 4")

def test_xfail5():
    print("xfail test 5")