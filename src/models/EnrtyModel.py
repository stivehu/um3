from src.models.RemoteApiModel import RemoteApiModel


class EntryModel(object):
    def __init__(self):
        self.__remoteApi = RemoteApiModel()
        self.errors=None

    def create_new_entry(self, param):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_create_entry_link(), 'post', param)
        if result != None:
            result.pop("rfid2", None)
            result.pop("id", None)
            result.pop("fragment", None)
        return result

    def setinthebox(self, mode, id):
        if self.check_id_is_exists(mode,id):
            result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.setinthebox_link( mode, id))

    def check_id_is_exists(self,mode,id):
        if self.__remoteApi.sendAjaxRequest(self.__remoteApi.idisexist_link(mode, id)):
            return True
        else:
            _translate = QtCore.QCoreApplication.translate
            self.errors = _translate("models", "Id not exists")

    #
    # def get_error_messages(self):
    #     if self.__remoteApi.error == None:
    #         return None
    #     else:
    #         return self.__remoteApi.error
