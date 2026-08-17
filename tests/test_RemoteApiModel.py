import json

import pytest, pytest_mock

import src.models.SettingsModel
from src.models.RemoteApiModel import RemoteApiModel
from src.models.SettingsModel import SettingsModel


def test_get_update_picking_bad_url():
    remoteApi = RemoteApiModel()
    assert None == remoteApi.get_update_pickeding_url('ABCEFG', "bad")


def test_get_agegroup_link(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    # SettingsModel.get_server_ip = MagicMock(return_value='192.168.0.115')
    remoteApiModel = RemoteApiModel()
    assert remoteApiModel.get_agegroup_link() == 'http://192.168.0.115/api/category/agegroup-index'


def test_get_update_pickeding_url(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    remoteApiModel = RemoteApiModel()
    assert remoteApiModel.get_update_pickeding_url('ABCED',
                                                   'up') == 'http://192.168.0.115/api/entry/update-by-rfid?rfid=ABCED&state=up'
    assert remoteApiModel.get_update_pickeding_url('ABCED',
                                                   'down') == 'http://192.168.0.115/api/entry/update-by-rfid?rfid=ABCED&state=down'
    assert remoteApiModel.get_update_pickeding_url('ABCED',
                                                   'down') == 'http://192.168.0.115/api/entry/update-by-rfid?rfid=ABCED&state=down'
    assert remoteApiModel.get_update_pickeding_url('ABCED', None) == None


def test_get_result_url(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    remoteApiModel = RemoteApiModel()
    assert remoteApiModel.get_result_url() == 'http://192.168.0.115/entry/result'


def test_get_scoreboard_url(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    remoteApiModel = RemoteApiModel()
    assert remoteApiModel.get_scoreboard_url('ABCED') == 'http://192.168.0.115/entry/scoreboard?rfid=ABCED'


def test_sendAjaxRequest_returns_none_on_json_decode_error(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    remoteApiModel = RemoteApiModel()
    fake_response = mocker.Mock()
    fake_response.status_code = 200
    fake_response.json.side_effect = json.JSONDecodeError("msg", "doc", 0)
    mocker.patch.object(remoteApiModel._RemoteApiModel__session, 'get', return_value=fake_response)

    result = remoteApiModel.sendAjaxRequest('http://192.168.0.115/api/entry/create', 'get')

    assert result is None
    assert remoteApiModel.error == "Server error"


def test_sendAjaxRequest_returns_none_on_io_error(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    remoteApiModel = RemoteApiModel()
    mocker.patch.object(remoteApiModel._RemoteApiModel__session, 'get', side_effect=IOError())

    result = remoteApiModel.sendAjaxRequest('http://192.168.0.115/api/entry/create', 'get')

    assert result is None
    assert remoteApiModel.error == "IO error"
