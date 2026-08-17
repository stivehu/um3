import pytest

from src.Timesync.src.TimeServer import TimeServer


def test_run_accepts_multiple_clients_sequentially(mocker):
    fake_listen_socket = mocker.Mock()
    mocker.patch('src.Timesync.src.TimeServer.socket.socket', return_value=fake_listen_socket)

    first_conn = mocker.Mock()
    first_conn.recv.side_effect = [b'ping', b'']

    fake_listen_socket.accept.side_effect = [
        (first_conn, ('127.0.0.1', 1)),
        OSError('stop'),
    ]

    server = TimeServer()

    with pytest.raises(OSError):
        server.run()

    assert fake_listen_socket.accept.call_count == 2
