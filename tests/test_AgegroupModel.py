
from src.models.AgegroupModel import AgegroupModel
from tests.fixtures.jsons import distances
from src.models.RemoteApiModel import RemoteApiModel
import pytest,pytest_mock


def test_agegroup_empty_model(mocker):
    mocker.patch('src.models.AgegroupModel.RemoteApiModel.sendAjaxRequest', return_value=None)
    agegroupModel = AgegroupModel()
    assert agegroupModel.get_agegroup_names() == []
    assert agegroupModel.get_agegroup_from_index() == -1


def test_agegroup_model(mocker):
    mocker.patch('src.models.AgegroupModel.RemoteApiModel.sendAjaxRequest', return_value=distances)
    agegroupModel = AgegroupModel()
    assert agegroupModel.get_agegroup_names == ['7-10 év', '11-14 év', '15-18 év', '19-30 év', '31-40 év',
                                                '41-50 év',
                                                '51-60 év', '61 év felettiek']
    assert agegroupModel.get_agegroup_from_index() == [2, 3, 10, 8, 6, 7, 5, 9]


def test_agegroup_model(mocker):
    mocker.patch('src.models.AgegroupModel.RemoteApiModel.sendAjaxRequest', return_value=distances)
    agegroupModel = AgegroupModel()
    assert agegroupModel.get_agegroup_from_age(42) == 7
    assert agegroupModel.get_agegroup_from_age(7) == 2
    assert agegroupModel.get_agegroup_from_age(8) == 2
    assert agegroupModel.get_agegroup_from_age(9) == 2
    assert agegroupModel.get_agegroup_from_age(10) == 2
    assert agegroupModel.get_agegroup_from_age(61) == 9
    assert agegroupModel.get_agegroup_from_age(62) == 9
    assert agegroupModel.get_agegroup_from_age(6) == None
    assert agegroupModel.get_agegroup_from_age(2) == None
    assert agegroupModel.get_agegroup_from_age(-2) == None


def test_get_agegroup_index(mocker):

    mocker.patch('src.models.AgegroupModel.RemoteApiModel.sendAjaxRequest', return_value=distances)
    agegroupModel = AgegroupModel()
    agegroupModel.get_agegroup_names()
    assert agegroupModel.get_agegroup_from_index(7) == 5
    assert agegroupModel.get_agegroup_from_index(2) == 0
    assert agegroupModel.get_agegroup_from_index(10) == 2
    assert agegroupModel.get_agegroup_from_index(1) == -1
    assert agegroupModel.get_agegroup_from_index(11) == -1
    assert agegroupModel.get_agegroup_from_index(-2) == -1
