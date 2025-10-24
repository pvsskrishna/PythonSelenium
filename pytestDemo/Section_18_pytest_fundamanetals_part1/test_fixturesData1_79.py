# Assume that we are testing the profile page where we need to send the first and last name.
# We are loading that data from fixture in conftest file
import pytest



@pytest.mark.usefixtures('dataLoad')
class TestExample2:
    def test_editProfile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])