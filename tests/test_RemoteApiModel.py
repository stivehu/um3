import unittest
from unittest.mock import MagicMock

from src.models.RemoteApiModel import RemoteApiModel
from src.models.SettingsModel import SettingsModel


class test_RemoteApiModel(unittest.TestCase):
    def test_get_update_picking_bad_url(self):
        remoteApi = RemoteApiModel()
        assert None == remoteApi.get_update_pickeding_url('ABCEFG', "bad")

    def test_get_agegroup_link(self):
        SettingsModel.real_get_server_ip = SettingsModel.get_server_ip
        SettingsModel.get_server_ip = MagicMock(return_value='192.168.0.115')
        remoteApiModel = RemoteApiModel()
        assert remoteApiModel.get_agegroup_link() == 'http://192.168.0.115/api/category/agegroup-index'
        SettingsModel.get_server_ip = SettingsModel.real_get_server_ip

    def test_get_update_pickeding_url(self):
        SettingsModel.real_get_server_ip = SettingsModel.get_server_ip
        SettingsModel.get_server_ip = MagicMock(return_value='192.168.0.115')
        remoteApiModel = RemoteApiModel()
        assert remoteApiModel.get_update_pickeding_url('ABCED',
                                                       'up') == 'http://192.168.0.115/api/entry/update-by-rfid?rfid=ABCED&state=up'
        assert remoteApiModel.get_update_pickeding_url('ABCED',
                                                       'down') == 'http://192.168.0.115/api/entry/update-by-rfid?rfid=ABCED&state=down'
        assert remoteApiModel.get_update_pickeding_url('ABCED',
                                                       'down') == 'http://192.168.0.115/api/entry/update-by-rfid?rfid=ABCED&state=down'
        assert remoteApiModel.get_update_pickeding_url('ABCED', None) == None
        SettingsModel.get_server_ip = SettingsModel.real_get_server_ip
