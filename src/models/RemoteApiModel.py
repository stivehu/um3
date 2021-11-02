import requests
from requests.exceptions import ConnectionError

from src.models.SettingsModel import SettingsModel


# from SettingsModel import SettingsModel


class RemoteApiModel(object):

    def __init__(self):
        self.__settings = SettingsModel()
        self.errors = []

    def get_update_pickeding_url(self, rfid, upordown):
        server = self.__settings.get_server_ip()
        if upordown == "up" or upordown == "down":
            return "http://{server}/api/entry/update-by-rfid?rfid={rfid}&state={upordown}".format(server=server,
                                                                                                  rfid=rfid,
                                                                                                  upordown=upordown)
        return None

    def get_entry_from_rfid(self, rfid):
        server = self.__settings.get_server_ip()
        return "http://{server}/api/entry/view-by-rfid?rfid={rfid}".format(server=server, rfid=rfid)

    def sendAjaxRequest(self, link, mode='get', params=None):
        try:
            if mode == "put":
                response = requests.put(link, params=params, timeout=1)
            elif mode == "get":
                response = requests.get(link, params=params, timeout=1)
            elif mode == "post":
                response = requests.post(link, params=params, timeout=1)
            if response.ok:
                return response.json()
        except ConnectionError:
            self.errors.append("Connection error")
        except IOError:
            self.errors.append("IO error")
        return None

    def __sendRequest(self, mode, link, params):
        if mode == "put":
            return requests.put(link, params=params, timeout=1)
        elif mode == "get":
            return requests.get(link, params=params, timeout=1)
        elif mode == "post":
            return requests.post(link, params=params, timeout=1)
