import requests
from requests.exceptions import ConnectionError

from src.models.SettingsModel import SettingsModel
from bs4 import BeautifulSoup
import json


class RemoteApiModel(object):

    def __init__(self):
        self.__settings = SettingsModel()
        self.error = ''
        self.__server = self.__settings.get_server_ip()
        self.status_code = 0
        self.__session = requests.session()

    def get_update_pickeding_url(self, rfid, upordown):
        if upordown == "up" or upordown == "down":
            return "http://{server}/api/entry/update-by-rfid?rfid={rfid}&state={upordown}".format(server=self.__server,
                                                                                                  rfid=rfid,
                                                                                                  upordown=upordown)
        return None

    def list_in_thebox_link(self):
        return "http://{server}/api/entry/listinthebox".format(server=self.__server)

    def setinthebox_link(self, mode, id):
        return "http://{server}/api/entry/setinthebox?mode={mode}&id={id}".format(server=self.__server, mode=mode,
                                                                                  id=id)

    def idisexist_link(self, mode, id):
        return "http://{server}/api/entry/idisexist?mode={mode}&id={id}".format(server=self.__server, mode=mode, id=id)

    def get_entry_from_rfid(self, rfid):
        return "http://{server}/api/entry/view-by-rfid?rfid={rfid}".format(server=self.__server, rfid=rfid)

    def create_entry_timestamp_from_rfid(self, rfid):
        return "http://{server}/api/entry/create-timestamp-from-rfid?rfid={rfid}".format(server=self.__server,
                                                                                         rfid=rfid)

    def get_distance_link(self):
        return "http://{server}/api/distance/index".format(server=self.__server)

    def get_agegroup_link(self):
        return "http://{server}/api/category/agegroup-index".format(server=self.__server)

    def get_gender_link(self):
        return "http://{server}/api/category/gender-index".format(server=self.__server)

    def get_create_entry_link(self):
        return "http://{server}/api/entry/create".format(server=self.__server)

    def get_entry_from_startnum(self, startnum):
        return "{server}/api/entry/view-from-startnum?startnum={startnum}".format(
            server=self.__settings.get_entry_site_url(),
            startnum=startnum)

    def get_login_url(self):
        return "{server}/myuser/login".format(server=self.__settings.get_entry_site_url())

    def get_update_rfid_from_startnum(self, startnum, rfid):
        return "{server}/api/entry/update-rfid-from-startnum?startnum={startnum}&rfid={rfid}" \
            .format(server=self.__settings.get_entry_site_url(), startnum=startnum, rfid=rfid)

    def get_logged_in_url(self):
        return "{server}/user/admin/index".format(server=self.__settings.get_entry_site_url())

    def login(self, login):
        response = self.__session.get(self.get_login_url())
        if response.status_code == 200:
            signin = BeautifulSoup(response._content, 'html.parser')
            login['_csrf'] = signin.find('meta', attrs={'name': 'csrf-token'})['content']
            login['ajax'] = 'login-form'
            self.__session.post(self.get_login_url(), data=login)
            response = self.__session.get(self.get_logged_in_url(), allow_redirects=False)
            if response.status_code == 200:
                return True
            else:
                self.error = response.reason
                self.status_code = response.status_code
                return False
        else:
            self.error = response.reason
            self.status_code = response.status_code
            return False

    def sendAjaxRequest(self, link, mode='get', params=None):
        response = None
        try:
            if mode == "put":
                response = self.__session.put(link, params=params, timeout=1, allow_redirects=False)
            elif mode == "get":
                response = self.__session.get(link, params=params, timeout=1, allow_redirects=False)
            elif mode == "post":
                response = self.__session.post(link, data=params, timeout=1, allow_redirects=False)
            if response.status_code == 200 or response.status_code == 201:
                self.status_code = response.status_code
                return response.json()
            else:
                self.error = json.loads(response.text)['message']
                self.status_code = response.status_code
                return None
        # except ConnectionError:
        #     self.error = "Connection error"
        except IOError:
            self.error = "IO error"
        except json.JSONDecodeError:
            self.error = "Server error"
            self.status_code = 451
        return response

    # def __sendRequest(self, mode, link, params):
    #     if mode == "put":
    #         return requests.put(link, params=params, timeout=1)
    #     elif mode == "get":
    #         return requests.get(link, params=params, timeout=1)
    #     elif mode == "post":
    #         return requests.post(link, params=params, timeout=1)
