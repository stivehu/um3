from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from src.models.RemoteApiModel import RemoteApiModel


class IntheboxModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super(IntheboxModel, self).__init__()
        self.__remoteApi = RemoteApiModel()
        self.__insert_pos = None
        self.__new_item = -1
        self.list()
        self.__rfid = None
        self.error = ''


    def set_inserting_item(self, value=-1):
        self.__new_item = value
        return self


    def get_inserting_item(self):
        return self.__insert_pos

    def list(self):
        response = self.__remoteApi.sendAjaxRequest(self.__remoteApi.list_in_thebox_link())
        self._data = []
        self._data.append([])
        if response == None:
            self.error = 'Server error'
            return None
        row = 0
        col = 0
        for startnum in response:
            if col >= 10:
                col = 1
                row = row + 1
                self._data.append([])
            else:
                col = col + 1
            self._data[row].append(startnum['startnum'])
            self.__save_insert_pos(row, col, startnum['startnum'])

        self.layoutChanged.emit()

    def __save_insert_pos(self, row, col, startnum):
        if startnum == self.__new_item:
            self.__insert_pos = [row, col]

    def count_all_record(self):
        return sum(len(x) for x in self._data)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            try:
                return self._data[index.row()][index.column()]
            except IndexError as e:
                pass

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
