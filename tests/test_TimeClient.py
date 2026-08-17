import base64
import datetime
import re

import pytest

from src.Timesync.src.TimeClient import TimeClient


def _decode_powershell_command(command):
    encoded = re.search(r'-EncodedCommand[\'",\s]*([A-Za-z0-9+/=]+)', command).group(1)
    return base64.b64decode(encoded).decode('utf-16-le')


def test_run_compensates_half_round_trip_delay(mocker):
    client = TimeClient()
    fake_socket = mocker.Mock()
    fake_socket.recv.return_value = b'1000.3 1000.0'
    mocker.patch('src.Timesync.src.TimeClient.socket.socket', return_value=fake_socket)
    mocker.patch('src.Timesync.src.TimeClient.time.time', side_effect=[1000.0, 1000.6])
    set_time_mock = mocker.patch.object(client, 'set_time')

    client.run()

    set_time_mock.assert_called_once_with(pytest.approx(1000.6))


def test_set_time_on_windows_requests_uac_elevation_and_sets_date(mocker):
    client = TimeClient()
    mocker.patch('src.Timesync.src.TimeClient.sys.platform', 'win32')
    system_mock = mocker.patch('src.Timesync.src.TimeClient.os.system')

    client.set_time(1700000000)

    command = system_mock.call_args.args[0]
    assert 'sudo' not in command
    assert 'powershell' in command

    outer_script = _decode_powershell_command(command)
    assert 'Start-Process' in outer_script
    assert '-Verb RunAs' in outer_script

    inner_script = _decode_powershell_command(outer_script)
    expected_local_time = datetime.datetime.fromtimestamp(1700000000).strftime('%Y-%m-%d %H:%M:%S')
    assert f"Set-Date -Date '{expected_local_time}'" in inner_script


def test_set_time_on_linux_uses_sudo_date(mocker):
    client = TimeClient()
    mocker.patch('src.Timesync.src.TimeClient.sys.platform', 'linux')
    system_mock = mocker.patch('src.Timesync.src.TimeClient.os.system')

    client.set_time(1700000000)

    command = system_mock.call_args.args[0]
    assert 'sudo date' in command
    assert 'powershell' not in command
