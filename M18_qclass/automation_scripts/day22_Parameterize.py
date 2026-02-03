#08/01/2025 --> Day20
"""
pytest
"""
from time import sleep
import pytest

"""
pytest:
*******
*pytest is a unit-testing framework basically developer will be used.
*pytest will be used by QA for following reason,
    *to run test function/method automatically.
    *to run multiple testcase at oneshot.
    *to generate reports.
    *to achieve parallel execution(compatibility).

steps to install pytest:
************************
click on file-->click on settings-->click on project-->click python interpreter-->click on plus icon
-->search for pytest-->click on specify version(latest version)-->click on install package.

naming convention for pytest:
*****************************
*function/method name should be starts with test keyword(test_*).
*class name should starts with Test keyword and 1st letter should be capital(Test_*) and pytest class should
not consist of constructor(__init__).
*module name can starts with test (or) end with test keyword(test_* (or) *_test).

how to run pytest function/class:
*********************************
*copy the path where pytest function/file is present(right click on folder-->click on copy path-->click on absolute path)
*open cmd --> change directory by below command
    >>cd path_of_pytest_file
    >>pytest -vs pytest_filename.py

v->verbosity
s->scripting    
*vs is used to get the output/message in detailed format.

right click on file --> click on open in -->click on terminal-->type the command

note:
-----
*a function which starts with test keyword is called as test function/method
*a class which starts with test keyword is called as test class.
*a module start/end with test keyword is called as test module.
"""

#calling a function
"""
def sample():
    print("sample testcase")

sample()
#sample testcase
"""

#calling a method
"""
class Demo:
    def simple(self):
        print("simple testcase")

d = Demo()
d.simple()
#simple testcase
""""""
*according to above example function and method will bet execute when ever we are calling explicitly.
*if we want to execute a function/method without calling explicitly then we need go for "pytest" concept.
"""
#####################################################################################################
#function level
#test function
"""
def test_TC1():
    print("testcase1 function")
def test_TC2():
    print("testcase2 function")
"""
"""
>pytest -vs pytestconcept.py
collected 2 items

pytestconcept.py::test_TC1 testcase1 function
PASSED
pytestconcept.py::test_TC2 testcase2 function
PASSED
"""
#non-test function
"""
def TC1_test():
    print("testcase1 function")
def test_TC2():
    print("testcase2 function")
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::test_TC2 testcase2 function
PASSED
"""
#non-test function
"""
def TC1():
    print("testcase1 function")
def TC2():
    print("testcase2 function")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
"""
##################################################################################################
#class and method level
#non-testclass and test method
"""
class Sample:
    def test_m1(self):
        print("method1 testcase")
    def test_m2(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
"""
#testclass and test method
"""
class TestSample:
    def test_m1(self):
        print("method1 testcase")
    def test_m2(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 2 items

pytestconcept.py::TestSample::test_m1 method1 testcase
PASSED
pytestconcept.py::TestSample::test_m2 method2 testcase
PASSED
"""
#testclass and non-test method
"""
class TestSample:
    def m1(self):
        print("method1 testcase")
    def m2(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
"""
#testclass and non-test method
"""
class TestSample:
    def test_m1(self):
        print("method1 testcase")
    def m2_test(self):
        print("method2 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::TestSample::test_m1 method1 testcase
PASSED
"""
##########################################################################################
#class level
"""
class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def test_m2(self):
        print("m2 testcase2")

class TestSimple:
    def test_m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::TestSample::test_m1 m1 testcase1
PASSED
pytestconcept.py::TestSample::test_m2 m2 testcase2
PASSED
pytestconcept.py::TestSimple::test_m3 m3 testcase1
PASSED
pytestconcept.py::TestSimple::test_m4 m4 testcase2
PASSED
"""
#non-test class andnon-test method
"""
class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def test_m2(self):
        print("m2 testcase2")

class SimpleTest:
    def test_m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")
"""
"""
>pytest -vs pytestconcept.py
collected 2 items

pytestconcept.py::TestSample::test_m1 m1 testcase1
PASSED
pytestconcept.py::TestSample::test_m2 m2 testcase2
PASSED
"""
#non-test class andnon-test method
"""
class TestSample:
    def test_m1(self):
        print("m1 testcase1")
    def m2(self):
        print("m2 testcase2")

class SimpleTest:
    def m3(self):
        print("m3 testcase1")
    def test_m4(self):
        print("m4 testcase2")
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::TestSample::test_m1 m1 testcase1
PASSED
"""
#test class consist of constructor
"""
class TestDemo:
    def __init__(self):
        print("im a constructor")
    def test_m1(self):
        print("m1 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items
 PytestCollectionWarning: cannot collect test class 'TestDemo'
because it has a __init__ constructor (from: pytestconcept.py)
"""
############################################################################################
#module level
"""
def test_fun1():
    print("testcase function")

class TestGmail:
    def test_compose(self):
        print("compos testcase")
    def test_inbox(self):
        print("inbox testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_fun1 testcase function
PASSED
pytestconcept.py::TestGmail::test_compose compos testcase
PASSED
pytestconcept.py::TestGmail::test_inbox inbox testcase
PASSED
"""
############################################################################################################
############################################################################################################

#01/08/2025 ---> Day 21
"""
markers:
--------
*markers are used to execute the specific test function/method/class/module.
*pytest markers are classified into 2 types,
    1.custom markers
    2.built-in markers

Pytest custom markers
=====================
 @pytest.mark is a decorator used to add the metadata to the test.
 Metadata : details about the data.
Grouping test cases using custom markers
 We can create custom markers by using, @pytest.mark.markerName
 We can group the test cases.
 To execute: pytest filename.py –vs –m “name of the marker”

 To execute multiple markers: 
o pytest filename.py –vs –m “marker1 or marker2”  executes testcases which are 
marked with either marker1 or marker2
o pytest filename.py –vs –m “marker1 and marker2”  executes the testcases which are 
marked with both marker1 and marker2.
o pytest filename.py –vs –m “not marker2”  executes the testcases which are not 
marked with marker2.
"""
# function level
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
# executing which are marked with p3
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
def test_trash():
    print("tash testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "p3" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::test_trash tash testcase
PASSED
pytestconcept.py::test_bin bin testcase
PASSED
"""
# executing which are marked with smoke
"""
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
"""
"""
>pytest -vs -m "smoke" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_trash tash testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
# executing which are marked with regression
"""
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
"""
"""
>pytest -vs -m "regression" pytestconcept.py
collected 4 items / 4 deselected / 0 selected
"""
# example on writing multiple marker name
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "reg, smoke" pytestconcept.py
collected 4 items
ERROR: Wrong expression passed to '-m': reg, smoke: at column 4: unexpected character ","
"""
# executing smoke and p3 marker
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke and p3" pytestconcept.py
collected 4 items / 3 deselected / 1 selected

pytestconcept.py::test_trash tash testcase
PASSED
"""
# executing smoke or reg marker
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "smoke or reg" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_trash tash testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
# executing excluding m3 marker
"""
@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("tash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")
"""
"""
>pytest -vs -m "not p3" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::test_login loginpage testcase
PASSED
pytestconcept.py::test_compose compose testcase
PASSED
"""
#################################################################################################
# method level
# executing only regression marker
"""
class TestInsta:
    @pytest.mark.regression
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    def test_chat(self):
        print("chat testcase")
"""
"""
>pytest -vs -m "regression" pytestconcept.py
collected 3 items / 1 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_chat chat testcase
PASSED
"""
# executing only regression marker
"""
class TestInsta:
    @pytest.mark.regression
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    def chat(self):
        print("chat testcase")
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "regression" pytestconcept.py
collected 3 items / 2 deselected / 1 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
"""
# executinh regression and high marker
"""
class TestInsta:
    @pytest.mark.regression
    @pytest.mark.high
    def test_post(self):
        print("post testcase")
    @pytest.mark.critical
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    @pytest.mark.low
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.high
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "regression and high" pytestconcept.py
collected 4 items / 3 deselected / 1 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
"""
# executinh regression or high marker
"""
class TestInsta:
    @pytest.mark.regression
    @pytest.mark.high
    def test_post(self):
        print("post testcase")
    @pytest.mark.critical
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    @pytest.mark.low
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.high
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "regression or high" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_chat chat testcase
PASSED
pytestconcept.py::TestInsta::test_register register testcase
PASSED
"""
##############################################################################################
# class level
# executinh which are marked with imp
"""
@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    def test_chat(self):
        print("chat testcase")
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "imp" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_story story testcase
PASSED
"""
# executinh which are marked with imp
"""
@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    def test_chat(self):
        print("chat testcase")
@pytest.mark.imp
class TestSample:
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "imp" pytestconcept.py
collected 4 items / 1 deselected / 3 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_story story testcase
PASSED
pytestconcept.py::TestSample::test_register register testcase
PASSED
"""
# executing class except mark with imp
"""
@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    def test_chat(self):
        print("chat testcase")
@pytest.mark.imp
class TestSample:
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "not imp" pytestconcept.py
collected 4 items / 3 deselected / 1 selected

pytestconcept.py::TestFb::test_chat chat testcase
PASSED
"""
# combination of class level and method level marker
"""
@pytest.mark.imp
class TestInsta:
    @pytest.mark.m1
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    @pytest.mark.m2
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.m1
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "m1" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestFb::test_register register testcase
PASSED
"""
# combination of class level and method level marker
"""
@pytest.mark.imp
class TestInsta:
    @pytest.mark.m1
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class TestFb:
    @pytest.mark.m2
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.m1
    def test_register(self):
        print("register testcase")
"""
"""
>pytest -vs -m "imp" pytestconcept.py
collected 4 items / 2 deselected / 2 selected

pytestconcept.py::TestInsta::test_post post testcase
PASSED
pytestconcept.py::TestInsta::test_story story testcase
PASSED
"""

# single function multiple markers
"""
@pytest.mark.m1
@pytest.mark.m2
@pytest.mark.m3
@pytest.mark.m4
@pytest.mark.m5
@pytest.mark.m6
def test_chat():
    print("chat testcase")
"""
"""
>pytest -vs -m "m5" pytestconcept.py
collected 1 item

pytestconcept.py::test_chat chat testcase
PASSED
"""
################################################################################################
# module level
# marking for entire module
"""
pytestmark = pytest.mark.smoke

def test_fun1():
    print("funtion testcase")

class TestSample:
    def test_tc1(self):
        print("test method1")
    def test_tc2(self):
        print("test method2")
"""
"""
>pytest -vs -m "smoke" pytestconcept.py
collected 3 items

pytestconcept.py::test_fun1 funtion testcase
PASSED
pytestconcept.py::TestSample::test_tc1 test method1
PASSED
pytestconcept.py::TestSample::test_tc2 test method2
PASSED
"""
#########################################################################################
"""
built-in markers:
----------------
1.skip
2.skipif
3.xfail
4.parameterize
5.usefixture
"""
"""
Skipping test functions
1. Skip
 The simplest way to skip a test function is to mark it with the skip decorator which may 
be passed an optional reason:
   @pytest.mark.skip(reason=””) : skips the testcases always without any reason
2. Skipif
  If you wish to skip something conditionally then you can use skipif instead.
  @pytest.mark.skipif(condition, reason): skips the testcases only when the condition is  True.
"""
#function level
"""
def test_tc1():
    print("testcase1")
@pytest.mark.skip
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
@pytest.mark.skip
def test_tc4():
    print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_tc1 testcase1
PASSED
pytestconcept.py::test_tc2 SKIPPED (unconditional skip)
pytestconcept.py::test_tc3 testcase3
PASSED
pytestconcept.py::test_tc4 SKIPPED (unconditional skip)
"""

"""
def test_tc1():
    print("testcase1")
@pytest.mark.skip(reason="low priority")
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
@pytest.mark.skip(reason="not important")
def test_tc4():
    print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_tc1 testcase1
PASSED
pytestconcept.py::test_tc2 SKIPPED (low priority)
pytestconcept.py::test_tc3 testcase3
PASSED
pytestconcept.py::test_tc4 SKIPPED (not important)
"""
#############################################################################################
"""
class TestSample:
    def test_tc1(self):
        print("testcase1")
    @pytest.mark.skip(reason="low priority")
    def test_tc2(self):
        print("testcase2")
    def test_tc3(self):
        print("testcase3")
    @pytest.mark.skip(reason="not important")
    def test_tc4(self):
        print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_tc1 testcase1
PASSED
pytestconcept.py::test_tc2 SKIPPED (low priority)
pytestconcept.py::test_tc3 testcase3
PASSED
pytestconcept.py::test_tc4 SKIPPED (not important)
"""

"""
@pytest.mark.skip(reason="all method are not required")
class TestSample:
    def test_tc1(self):
        print("testcase1")
    def test_tc2(self):
        print("testcase2")
class TestSimple:
    def test_tc3(self):
        print("testcase3")
    def test_tc4(self):
        print("testcase4")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::TestSample::test_tc1 SKIPPED (all method are not required)
pytestconcept.py::TestSample::test_tc2 SKIPPED (all method are not required)
pytestconcept.py::TestSimple::test_tc3 testcase3
PASSED
pytestconce
"""
#################################################################################################
#example on skipif
"""
testid = 3423
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_TC1 testcas1
PASSED
pytestconcept.py::test_TC2 SKIPPED (test_case not required)
pytestconcept.py::test_TC3 testcas3
PASSED
"""

"""
testid = 3428
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_TC1 testcas1
PASSED
pytestconcept.py::test_TC2 testcas2
PASSED
pytestconcept.py::test_TC3 testcas3
PASSED
"""

"""
class TestExe:
    os = "mac"
    def test_TC1(self):
        print("testcas1")
    @pytest.mark.skipif(os in ["linux", "window", "mac"], reason="platform missmatch")
    def test_TC2(self):
        print("testcas2")
    def test_TC3(self):
        print("testcas3")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::TestExe::test_TC1 testcas1
PASSED
pytestconcept.py::TestExe::test_TC2 SKIPPED (platform missmatch)
pytestconcept.py::TestExe::test_TC3 testcas3
PASSED
"""
"""
browser="IE"
class TestDemo:
    def test_Tc1(self):
        print("method1 testcase")
    def test_Tc2(self):
        print("method2 testcase")
@pytest.mark.skipif(browser=="IE", reason="IE not exists")
class TestSample:
    def test_Tc3(self):
        print("method3 testcase")
    def test_Tc4(self):
        print("method4 testcase")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::TestDemo::test_Tc1 method1 testcase
PASSED
pytestconcept.py::TestDemo::test_Tc2 method2 testcase
PASSED
pytestconcept.py::TestSample::test_Tc3 SKIPPED (IE not exists)
pytestconcept.py::TestSample::test_Tc4 SKIPPED (IE not exists)
"""
###################################################################################################
"""
XFail
=====
 mark test functions as expected to fail
 You can use the xfail marker to indicate that you expect a test to fail:
Syntax: @pytest.mark.xfail([parameters])

1. condition parameter : If a test is only expected to fail under a certain condition, you can pass 
that condition as the first parameter:
Eg:
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function():
    . . .

2. reason parameter: You can specify the motive of an expected failure with 
the reason parameter
Eg:
@pytest.mark.xfail(reason="known parser issue")
def test_function():
    . . .

3. raises parameter: If you want to be more specific as to why the test is failing, you can specify 
a single exception, or a tuple of exceptions, in the raises argument.
Eg: 
@pytest.mark.xfail(raises=RuntimeError)
def test_function():
    . . .
note:
*****
*this marker will go when intenstaionally we want to fail the testcase because a feature is not stable/
new feature/not implemented/open defect/reqt changes etc.. 
*it will not print "fail" in result it will print as "xpass".
"""

"""
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail
def test_channel():
    print("channel module")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
XPASS
"""

"""
brw = "IE"
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail(brw in ["mozilla","chrome", "IE"], reason="not implemented")
def test_channel():
    print("channel module")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
XPASS (not implemented)
"""

"""
brw = "safari"
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail(brw in ["mozilla","chrome", "IE"], reason="not implemented")
def test_channel():
    print("channel module")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
PASSED
"""
"""
note:
*****
*in xfail marker if cond the is True then the result is "xpass" else if the cond is False the result
is "PASSED".
"""
######################################################################################################
#09/01/2026 ---> Day 22
"""
parameterize:
-------------
@pytest.mark.parametrize: The builtin pytest.mark.parametrize decorator enables parametrization 
of arguments for a test function.
Here is a typical example of a test function that implements checking that a certain input leads to an 
expected output
note:
-----
*in "parametrize" the number of names must be equal to the number of values.

syntax:-
========
@pytest.mark.parametrize("value1, value2", [[val1, val2], [val3, val4],....])
def func(value1, value2):
     . . .

note:
-----
*no. of variable should be equal to no. of values.
*no. of test function call equal to no. of inputs/values.
*when ever we are declaring multiple variables then multiple variables should be enclosed within
any brackets like tuple, list, set.
"""

"""
def add():
    a = 10
    b = 20
    print(a+b)
add()       #30
add()       #30
"""

"""
def add(a, b):
    print(a+b)
add(4, 8)       #12
add(7, 1)       #8
add(9, 2)       #11
"""
#according to above function add is a normal function, it will accept parameters when we call a function.
#but if it is test function we can't pass a argument bcz test function are not explicitly callable.
#for any test function/method if we pass any argument then it will consider as a fixture.

"""
def test_add(a, b):
    print(a+b)
test_add(2, 3)
"""
"""
>pytest -vs pytestconcept.py
collected 1 item

pytestconcept.py::test_add ERROR
fixture 'a' not found
"""
#to over come above drawback we use "parameterize" as builtin marker.
"""
@pytest.mark.parametrize("a", [10, 20, 30, 40])
def test_add(a):
    print(f"input is {a}")
"""
"""
>pytest -vs pytestconcept.py
collected 4 items

pytestconcept.py::test_add[10] input is 10
PASSED
pytestconcept.py::test_add[20] input is 20
PASSED
pytestconcept.py::test_add[30] input is 30
PASSED
pytestconcept.py::test_add[40] input is 40
PASSED
"""
#function level
"""
@pytest.mark.parametrize("a, b", [[10, 20], [2, 8], [8, 4]])
def test_add(a, b):
    print(f"result is:{a+b}")
"""
"""
>pytest -vs pytestconcept.py
collected 3 items

pytestconcept.py::test_add[10-20] result is:30
PASSED
pytestconcept.py::test_add[2-8] result is:10
PASSED
pytestconcept.py::test_add[8-4] result is:12
PASSED
"""

"""
@pytest.mark.parametrize("a, b", [[10, 20], [2, 8], [8, 4]])
def test_add(c, b):
    print(f"result is:{c+b}")
"""
"""
>pytest -vs pytestconcept.py
collected 0 items / 1 error

======================================================== ERRORS =========================================================
___________________________________________ ERROR collecting pytestconcept.py ___________________________________________
In test_add: function uses no argument 'a'
"""

"""
@pytest.mark.parametrize("a, b, c", [[10, 20], [2, 8], [8, 4]])
def test_add(a, b, c):
    print(f"result is:{a+b+c}")
"""
"""
>pytest -vs pytestconcept.py
pytestconcept.py::test_add: in "parametrize" the number of names (3):
  ['a', 'b', 'c']
must be equal to the number of values (2):
  [10, 20]
"""
#method level
"""
class Test_Demo:
    @pytest.mark.parametrize(["a", "b"], [["hey", "bye"], ["class", "over"]])
    def test_tc1(self, a, b):
        print(a, b)
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Demo::test_tc1[hey-bye] hey bye
PASSED
pyconcept.py::Test_Demo::test_tc1[class-over] class over
PASSED
"""
##########################################################################################
#script to create multiple account in jeevansathi.com
"""
@pytest.mark.parametrize("relation, gender, email, mob, pwd", [("Self", "Male", "akash98734@gmail.com", "9897969594", "Akash@1234^"),
                                                               ("Son", "Male", "amith4567@gmail.com", "8877665544", "AMIth@#$123"),
                                                               ("Daughter", "Female", "ganuganu34@gmail.com", "8687898085","GaNu@346%")])
def test_register(relation, gender, email, mob, pwd):
    driver = Chrome(options=o)
    driver.get("https://www.jeevansathi.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("id", "relationshipBlock").click()
    driver.find_element("xpath", f"//li[text()='{relation}']").click()
    if relation == "Self":
        driver.find_element("id", "gender").click()
        driver.find_element("xpath", f"//li[text()='{gender}']").click()
    driver.find_element("id", "email").send_keys(email)
    driver.find_element("id", "phoneNumber").send_keys(mob)
    driver.find_element("id", "password").send_keys(pwd)
    driver.find_element("xpath", "(//button[text()='Register for Free'])[2]").click()
    sleep(3)
    driver.close()
"""
#ws to pass different product and print all there product names
"""
@pytest.mark.parametrize("product", ["wedding gift", "baby", "book lover gifts", "host gift"])
def test_Etsy(product):
    driver = Chrome(options=o)
    driver.get("https://www.etsy.com/in-en/?ref=lgo")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("id", "global-enhancements-search-query").send_keys(product+Keys.ENTER)
    products = driver.find_elements("xpath", "//h3[contains(@id, 'listing-title-')]")
    for i in products:
        print(i.text)
    sleep(5)
    driver.close()
"""
#ws to login for instagram.com with multiple set of inputs
"""
@pytest.mark.parametrize("un, pwd", [["lokesh", "lokesh@1234"],
                                     ["mahesh", "mahesh@12123"],
                                     ["kumar", "kumar@!2334"]])
def test_login(un, pwd):
    driver = Chrome(options=o)
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("name", "username").send_keys(un)
    driver.find_element("name", "password").send_keys(pwd)
    driver.find_element("xpath", "//div[.='Log in']").click()
    sleep(3)
    driver.close()
"""