import json

from src.models.EntrypickupModel import EntrypickupModel


def test_check_format():
    with open("fixtures/entries-pickedup.json") as json_file:
        okresult = json.load(json_file)
        assert EntrypickupModel.checkFormat(okresult) == True
    badresult = okresult
    for removeitem in {"distance", "startnum", "firstname", "lastname", "gender", "agegroup", "pickedUp",
                       "pickedupstate"}:
        badresult.pop(removeitem, None)
        assert EntrypickupModel.checkFormat(badresult) == False
    assert EntrypickupModel.checkFormat(None) == False
