from src.models.RemoteApiModel import RemoteApiModel


class EntrypickupModel(object):

    def __init__(self):
        self.__remoteApi = RemoteApiModel()

    def get_entry_from_rfid(self, rfid):
        return self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_entry_from_rfid(rfid))

    def updateEntryPickedUp(self, rfid):
        return self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_update_pickeding_url(rfid, 'up'))

    def updateEntryPickedDown(self, rfid):
        return self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_update_pickeding_url(rfid, 'down'))

    @staticmethod
    def checkFormat(entrydatas):
        if not isinstance(entrydatas, dict):
            return False
        if {"distance", "startnum", "firstname", "lastname", "gender", "agegroup", "pickedUp",
            "pickedupstate"} <= entrydatas.keys():
            return True
        return False
