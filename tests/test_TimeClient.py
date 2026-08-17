import pytest

from src.Timesync.src.TimeClient import TimeClient


def test_run_compensates_half_round_trip_delay(mocker):
    client = TimeClient()
    fake_socket = mocker.Mock()
    fake_socket.recv.return_value = b'1000.3 1000.0'
    mocker.patch('src.Timesync.src.TimeClient.socket.socket', return_value=fake_socket)
    mocker.patch('src.Timesync.src.TimeClient.time.time', side_effect=[1000.0, 1000.6])
    set_time_mock = mocker.patch.object(client, 'set_time')

    client.run()

    set_time_mock.assert_called_once_with(pytest.approx(1000.6))
