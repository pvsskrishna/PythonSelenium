#install pytest
import pytest


# Any pytest file name should start with test_ or end with _test
# pytest method names should start with test
#anycode should be wrapped in method only

@pytest.mark.smoke
def test_firstprogram():
    print('hello')

@pytest.mark.skip
@pytest.mark.smoke
def test_thirdprogram():
    print('Good afternoon')

def test_CreditCard1():
    print("Credit1")
