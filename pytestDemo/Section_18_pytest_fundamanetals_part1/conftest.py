import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing 1st")
    yield
    print(" I will be executing last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Varun","Paladugula","varunpaladugula.com"]

@pytest.fixture(params=['Chrome','Firefox','IE'])
def crossBrowser(request):
    return request.param

@pytest.fixture(params=[('Chrome','Varun','Paladugula'),('Firefox','Krishna'),'IE'])
def crossBrowser1(request):
    return request.param