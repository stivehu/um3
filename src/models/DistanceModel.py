import datetime

from PyQt5 import QtCore

from src.models.RemoteApiModel import RemoteApiModel


class DistanceModel(object):

    def __init__(self):
        self.__remoteApi = RemoteApiModel()
        response = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_distance_link())
        self.__distance_index = None
        if None == response:
            self.error = QtCore.QCoreApplication.translate("models", "Server error")
            self.__distances = None
        else:
            self.__distance_index = []
            self.__distances = response

    def get_distance_names(self):
        if self.__distances == None:
            return []
        result = []
        try:
            for distance in self.__distances:
                result.append(distance['name'])
                self.__distance_index.append(distance['id'])
        except TypeError:
            pass
        return result

    def get_distance_index(self):
        return self.__distance_index

    def get_age_from_birthday(self, birthday: str):
        act_year = datetime.datetime.now().year
        birth_year = datetime.datetime.strptime(birthday, "%Y-%m-%d").date().year
        return act_year - birth_year
