#install pytest
import pytest


# Any pytest file name should start with test_ or end with _test
# pytest method names should start with test
#anycode should be wrapped in method only


def test_secondprogram():
    msg = 'Good Morning'
    assert msg == 'hi', "Test failed because strings are not matching"
    #here the "Test failed because strings are not matching" this message will display when assert failed

@pytest.mark.smoke
def test_fourthprogram():
    a = 2
    b = 6
    assert a+4 == 6,"Summation is not matching"


def test_CreditCard2():
    print("Credit2")