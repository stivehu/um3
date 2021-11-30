from src.models.RemoteApiModel import RemoteApiModel


class EntrypickupModel(object):

    def __init__(self):
        self.__remoteApi = RemoteApiModel()
        self.error = None

    def get_entry_from_rfid(self, rfid):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_entry_from_rfid(rfid))
        self.error = self.__remoteApi.error
        return result

    def updateEntryPickedUp(self, rfid):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_update_pickeding_url(rfid, 'up'))
        self.error = self.__remoteApi.error
        return result

    def updateEntryPickedDown(self, rfid):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_update_pickeding_url(rfid, 'down'))
        self.error = self.__remoteApi.error
        return result

    @staticmethod
    def checkFormat(entrydatas):
        if not isinstance(entrydatas, dict):
            return False
        if {"distance", "startnum", "firstname", "lastname", "gender", "agegroup", "pickedUp",
            "pickedupstate"} <= entrydatas.keys():
            return True
        return False
