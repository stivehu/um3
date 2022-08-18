import os
import sys

import pytest, pytest_mock
from src.models.SettingsModel import SettingsModel


def test_settings_model():
    settings = SettingsModel()
    assert settings.get_server_ip() == '192.168.0.115'
    assert settings.get_chipcontroll_interval() == 1000
    assert settings.get_chipcontroll_wait_after_read() == 1500
    assert settings.get_auto_maximize_opening_window() == False
    assert settings.get_auto_resize_window() == False
    __remove_conf()


def test_settings_on_win32(mocker):
    mocker.patch.object(sys, 'platform', 'win32')
    settings = SettingsModel()
    assert settings.get_comm_port() == 'COM3'
    __remove_conf()


def test_settings_on_linux(mocker):
    mocker.patch.object(sys, 'platform', 'linux')
    settings = SettingsModel()
    assert settings.get_comm_port() == '/dev/ttyUSB0'
    __remove_conf()


def test_settings_model_setters():
    settings = SettingsModel()
    settings.set_server_ip("192.168.50.10")
    assert settings.get_server_ip() == "192.168.50.10"
    assert settings.get_server_ip() != "192.168.0.115"

    settings.set_chipcontroll_interval(2000)
    assert settings.get_chipcontroll_interval() == 2000

    settings.set_chipcontroll_wait_after_read(3000)
    assert settings.get_chipcontroll_wait_after_read() == 3000

    settings.set_auto_maximize_opening_window(False)
    assert settings.get_auto_maximize_opening_window() == False

    settings.set_auto_maximize_opening_window(True)
    assert settings.get_auto_maximize_opening_window() == True

    settings.set_auto_resize_window(False)
    assert settings.get_auto_resize_window() == False

    settings.set_auto_resize_window(True)
    assert settings.get_auto_resize_window() == True

    settings.set_comm_port('COM1')
    assert settings.get_comm_port() == 'COM1'
    __remove_conf()


def test_save_config():
    __remove_conf()
    settings = SettingsModel()
    settings \
        .set_server_ip("192.168.5.10") \
        .set_chipcontroll_interval(2500) \
        .set_chipcontroll_wait_after_read(3500) \
        .set_auto_maximize_opening_window(False) \
        .set_auto_resize_window(False) \
        .set_comm_port('COM9')
    settings.save_config()
    savedsettings = SettingsModel()
    assert savedsettings.get_server_ip() == "192.168.5.10"
    assert savedsettings.get_chipcontroll_interval() == 2500
    assert savedsettings.get_chipcontroll_wait_after_read() == 3500
    assert savedsettings.get_auto_maximize_opening_window() == False
    assert savedsettings.get_auto_resize_window() == False
    assert savedsettings.get_comm_port() == 'COM9'
    __remove_conf()


def __remove_conf():
    try:
        os.remove('um.conf')
    except OSError:
        pass
