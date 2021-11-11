from PyQt5 import QtCore

from src.models.RemoteApiModel import RemoteApiModel


class GenderModel(object):

    def __init__(self):
        self.__remoteApi = RemoteApiModel()
        response = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_gender_link())
        self.__gender_index = None
        if None == response:
            _translate = QtCore.QCoreApplication.translate
            self.error = _translate("models", "Server error")
            self.__genders = None
        else:
            self.__gender_index = []
            self.__genders = response

    def get_gender_names(self):
        if self.__genders == None:
            return []
        result = []
        try:
            for gender in self.__genders:
                result.append(gender['name'])
                self.__gender_index.append(gender['id'])
        except TypeError:
            pass
        return result

    def get_gender_index(self):
        return self.__gender_index
