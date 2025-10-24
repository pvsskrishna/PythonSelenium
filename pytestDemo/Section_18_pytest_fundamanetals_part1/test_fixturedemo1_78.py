import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemoMethod1(self):
        print("I will be executing the fixture demo method 1")

    def test_fixtureDemoMethod2(self):
        print("I will be executing the fixture demo method 2")

    def test_fixtureDemoMethod3(self):
        print("I will be executing the fixture demo method 3")

    def test_fixtureDemoMethod4(self):
        print("I will be executing the fixture demo method 4")