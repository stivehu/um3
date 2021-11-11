from src.models.RemoteApiModel import RemoteApiModel


class EntryModel(object):
    def __init__(self):
        self.__remoteApi = RemoteApiModel()

    def create_new_entry(self, param):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_create_entry_link(), 'post', param)
        if result != None:
            result.pop("rfid2", None)
            result.pop("id", None)
            result.pop("fragment", None)
        return result

    def get_error_messages(self):
        if (self.__remoteApi.errors == None):
            return None
        else:
            return self.__remoteApi.errors
