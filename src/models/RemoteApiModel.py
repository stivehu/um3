import requests
from requests.exceptions import ConnectionError

from src.models.SettingsModel import SettingsModel


class RemoteApiModel(object):

    def __init__(self):
        self.__settings = SettingsModel()
        self.error = ''
        self.__server = self.__settings.get_server_ip()

    def get_update_pickeding_url(self, rfid, upordown):
        if upordown == "up" or upordown == "down":
            return "http://{server}/api/entry/update-by-rfid?rfid={rfid}&state={upordown}".format(server=self.__server,
                                                                                                  rfid=rfid,
                                                                                                  upordown=upordown)
        return None

    def list_in_thebox_link(self):
        return "http://{server}/api/entry/listinthebox".format(server=self.__server)

    def setinthebox_link(self,mode,id):
        return "http://{server}/api/entry/setinthebox?mode={mode}&id={id}".format(server=self.__server,mode=mode,id=id)

    def idisexist_link(self,mode,id):
        return "http://{server}/api/entry/idisexist?mode={mode}&id={id}".format(server=self.__server,mode=mode,id=id)


    def get_entry_from_rfid(self, rfid):
        return "http://{server}/api/entry/view-by-rfid?rfid={rfid}".format(server=self.__server, rfid=rfid)

    def get_distance_link(self):
        return "http://{server}/api/distance/index".format(server=self.__server)

    def get_agegroup_link(self):
        return "http://{server}/api/category/agegroup-index".format(server=self.__server)

    def get_gender_link(self):
        return "http://{server}/api/category/gender-index".format(server=self.__server)

    def get_create_entry_link(self):
        return "http://{server}/api/entry/create".format(server=self.__server)

    def sendAjaxRequest(self, link, mode='get', params=None):
        response = None
        try:
            if mode == "put":
                response = requests.put(link, params=params, timeout=1)
            elif mode == "get":
                response = requests.get(link, params=params, timeout=1)
            elif mode == "post":
                response = requests.post(link, data=params, timeout=1)
            if response.ok:
                return response.json()
            else:
                self.error = response.json()
        except ConnectionError:
            self.error = "Connection error"
        except IOError:
            self.error = "IO error"
        return response

    def __sendRequest(self, mode, link, params):
        if mode == "put":
            return requests.put(link, params=params, timeout=1)
        elif mode == "get":
            return requests.get(link, params=params, timeout=1)
        elif mode == "post":
            return requests.post(link, params=params, timeout=1)
