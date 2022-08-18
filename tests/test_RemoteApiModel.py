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
