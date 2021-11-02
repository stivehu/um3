import unittest

from src.models.RemoteApiModel import RemoteApiModel


class test_RemoteApiModel(unittest.TestCase):

    def test_get_update_picked_up_url(self):
        remoteApi = RemoteApiModel()
        assert remoteApi.get_update_pickeding_url('ABCEFG',
                                                  "up") == "http://localhost/api/entry/update-by-rfid?rfid=ABCEFG&state=up"

    def test_get_update_picked_down_url(self):
        remoteApi = RemoteApiModel()
        assert remoteApi.get_update_pickeding_url('ABCEFG',
                                                  "down") == "http://localhost/api/entry/update-by-rfid?rfid=ABCEFG&state=down"

    def test_get_update_picking_bad_url(self):
        remoteApi = RemoteApiModel()
        assert None == remoteApi.get_update_pickeding_url('ABCEFG', "bad")

    def test_send_ajax_request_error(self):
        remoteApiModel = RemoteApiModel()
        response = remoteApiModel.sendAjaxRequest("http://www.veryberynotgoodaddess.com")
        self.assertEqual(remoteApiModel.errors, ["Connection error"])
        self.assertEqual(response, None)
