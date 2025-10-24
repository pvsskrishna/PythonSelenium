import pytest


def test_CreditCard1():
    print("Credit1")


@pytest.fixture
def setup():
    print("I will be executed first")
    yield
    print('I will be executing last')


def test_testFixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")