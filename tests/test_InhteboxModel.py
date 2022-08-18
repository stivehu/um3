from unittest import TestCase
import pytest,pytest_mock

from src.models.IntheboxModel import IntheboxModel
from src.models.RemoteApiModel import RemoteApiModel


# class TestInhteboxModel(TestCase):
mock_ajaxrequest = [{"startnum": 5002}, {"startnum": 5010}, {"startnum": 5043}, {"startnum": 5082},
                    {"startnum": 5104}, {"startnum": 5109}, {"startnum": 5124}, {"startnum": 5150},
                    {"startnum": 5166}, {"startnum": 10009}, {"startnum": 10010}, {"startnum": 10015},
                    {"startnum": 10016}, {"startnum": 10049}, {"startnum": 10056}, {"startnum": 10063},
                    {"startnum": 10073}, {"startnum": 10089}, {"startnum": 10093}, {"startnum": 10094}]
result = [[5002, 5010, 5043, 5082, 5104, 5109, 5124, 5150, 5166, 10009],
          [10010, 10015, 10016, 10049, 10056, 10063, 10073, 10089, 10093, 10094]]


def test_list(mocker):
    # RemoteApiModel.sendAjaxRequest = MagicMock(return_value=mock_ajaxrequest)
    mocker.patch('src.models.AgegroupModel.RemoteApiModel.sendAjaxRequest', return_value=mock_ajaxrequest)
    intheboxmodel = IntheboxModel()
    intheboxmodel.list()
    assert intheboxmodel._data == result
    assert intheboxmodel.count_all_record() == 20
