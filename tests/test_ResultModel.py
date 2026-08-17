import pytest, pytest_mock

from src.models.ResultModel import ResultModel


def test_get_result_url(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    resultModel = ResultModel()
    assert resultModel.get_result_url() == 'http://192.168.0.115/entry/result'


def test_get_scoreboard_url(mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_server_ip', return_value="192.168.0.115")
    resultModel = ResultModel()
    assert resultModel.get_scoreboard_url('ABCED') == 'http://192.168.0.115/entry/scoreboard?rfid=ABCED'
