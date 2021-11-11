import json
from os import getcwd

from src.models.EntrypickupModel import EntrypickupModel


def test_check_format():
    with open("{cwd}/fixtures/entries-pickedup.json".format(cwd=getcwd())) as json_file:
        okresult = json.load(json_file)
        assert EntrypickupModel.checkFormat(okresult) == True
    badresult = okresult
    for removeitem in {"distance", "startnum", "firstname", "lastname", "gender", "agegroup", "pickedUp",
                       "pickedupstate"}:
        badresult.pop(removeitem, None)
        assert EntrypickupModel.checkFormat(badresult) == False
    assert EntrypickupModel.checkFormat(None) == False
