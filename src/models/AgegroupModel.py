import sys

from PyQt5 import QtCore

from src.models.RemoteApiModel import RemoteApiModel


class AgegroupModel(object):

    def __init__(self):
        self.__remoteApi = RemoteApiModel()
        response = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_agegroup_link())
        self.__agegroup_index = []
        self.__agegroup_names = []
        self.error = None
        if None == response:
            self.error = QtCore.QCoreApplication.translate("models", "Server error")
            self.__agegroups = None
        else:
            self.__agegroup_index = []
            self.__agegroups = response
            self.__sort_agegroups()
            self.__parse_agegroup_names()

    def __sort_agegroups(self):
        try:
            if self.__agegroups != None:
                self.__agegroups = sorted(self.__agegroups, key=lambda x: x['sortid'])
        except TypeError:
            pass
        except KeyError:
            pass

    def __parse_agegroup_names(self):
        if self.__agegroups == None:
            return []
        try:
            for agegroup in self.__agegroups:
                self.__agegroup_names.append(agegroup['name'])
                self.__agegroup_index.append(agegroup['id'])
        except TypeError:
            pass

    def get_agegroup_names(self):
        return self.__agegroup_names

    def get_agegroup_index(self):
        return self.__agegroup_index

    def get_agegroup_from_index(self, agegroup_id=-1):
        if len(self.__agegroup_index) == 0:
            return -1
        for key, index in zip(range(0, len(self.__agegroup_index)), self.__agegroup_index):
            if index == agegroup_id:
                return key
        return -1

    def get_agegroup_from_age(self, age: int):
        for agegroup in self.__agegroups:
            if int(agegroup['minage']) <= age <= int(agegroup['maxage']):
                return agegroup['id']
        return None
