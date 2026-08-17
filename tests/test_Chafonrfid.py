from unittest.mock import MagicMock

from src.chafonrfid.Chafonrfid import Chafonrfid


def test_get_tid_read_timeout_closes_port(mocker):
    transport = MagicMock()
    transport.read_frame.side_effect = TimeoutError('Nem érkezett válasz a soros porton (timeout)')
    mocker.patch.object(Chafonrfid, 'open_port', return_value=transport)

    chafon = Chafonrfid()
    result = chafon.get_tid()

    assert result is None
    assert chafon.error == "olvasási hiba"
    transport.close.assert_called_once()
