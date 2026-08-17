from src.models.EnrtyModel import EntryModel


def test_check_id_is_exists_true(mocker):
    mocker.patch('src.models.EnrtyModel.RemoteApiModel.sendAjaxRequest', return_value={'id': 1})
    entryModel = EntryModel()
    assert entryModel.check_id_is_exists('rfid', 1) is True


def test_check_id_is_exists_false(mocker):
    mocker.patch('src.models.EnrtyModel.RemoteApiModel.sendAjaxRequest', return_value=None)
    entryModel = EntryModel()
    assert entryModel.check_id_is_exists('rfid', 1) is None
    assert entryModel.errors == "Id not exists"
