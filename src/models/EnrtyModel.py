from src.models.RemoteApiModel import RemoteApiModel


class EntryModel(object):
    def __init__(self):
        self.__remoteApi = RemoteApiModel()
        self.errors = None

    def create_new_entry(self, param):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_create_entry_link(), 'post', param)
        if result != None:
            result.pop("rfid2", None)
            result.pop("id", None)
            result.pop("fragment", None)
        return result

    def setinthebox(self, mode, id):
        if self.check_id_is_exists(mode, id):
            result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.setinthebox_link(mode, id))

    def check_id_is_exists(self, mode, id):
        if self.__remoteApi.sendAjaxRequest(self.__remoteApi.idisexist_link(mode, id)):
            return True
        else:
            _translate = QtCore.QCoreApplication.translate
            self.errors = _translate("models", "Id not exists")

    def read_entry_from_startnum(self, startnum):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_entry_from_startnum(startnum))
        self.status_code = self.__remoteApi.status_code
        return result

    def checkentryResult(self, response):
        if 'response' in response and 'firstname' in response['response'] and 'lastname' in response['response'] and 'distance' in response['response'] :
            return True
        return False

    def loginSite(self, username, password):
        login = {'login-form[login]': username, 'login-form[password]': password}
        return self.__remoteApi.login(login)

    def update_rfid_from_startnum(self, startnum, rfid):
        result = self.__remoteApi.sendAjaxRequest(self.__remoteApi.get_update_rfid_from_startnum(startnum, rfid))
        self.status_code = self.__remoteApi.status_code
        self.error = self.__remoteApi.error
        return result
