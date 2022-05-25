import sys
from configparser import ConfigParser


class SettingsModel(object):

    def __init__(self):
        self.__config = ConfigParser()
        self.__config['DEFAULT'] = {
            "ServerIp": "192.168.0.115",
            "ChipcontrollInterval": 1000,
            "ChipcontrollWaitAfterRead": 1500,
            "AutoMaximizeOpeningWindow": False,
            "AutoResizeWindow": False,
            "CommPort": self.get_default_com_port(),
            "EntrySiteUrl": "https://www.polarsport.hu/",
            "EntrySiteUsername": False,
            "EntrySitePassword": False
        }
        self.__config.read("um.conf")

    def save_config(self):
        with open('um.conf', 'w') as configfile:
            self.__config.write(configfile)

    def get_default_com_port(self, base=True):
        result = None
        if sys.platform == "linux":
            result = "/dev/ttyUSB0" if base else "/dev/ttyUSB"
        elif sys.platform == "win32":
            result = "COM3" if base else 'COM'
        return result

    def get_server_ip(self):
        return self.__config['DEFAULT']['ServerIp']

    def set_server_ip(self, value):
        self.__config['DEFAULT']['ServerIp'] = str(value)
        return self

    def get_chipcontroll_interval(self):
        return int(self.__config['DEFAULT']['ChipcontrollInterval'])

    def set_chipcontroll_interval(self, value):
        self.__config['DEFAULT']['ChipcontrollInterval'] = str(value)
        return self

    def get_chipcontroll_wait_after_read(self):
        return int(self.__config['DEFAULT']['ChipcontrollWaitAfterRead'])

    def set_chipcontroll_wait_after_read(self, value):
        self.__config['DEFAULT']['ChipcontrollWaitAfterRead'] = str(value)
        return self

    def get_auto_maximize_opening_window(self):
        return self.__config['DEFAULT']['AutoMaximizeOpeningWindow'] == 'True'

    def set_auto_maximize_opening_window(self, value):
        if value == True:
            self.__config['DEFAULT']['AutoMaximizeOpeningWindow'] = 'True'
        else:
            self.__config['DEFAULT']['AutoMaximizeOpeningWindow'] = 'False'
        return self

    def get_auto_resize_window(self):
        return self.__config['DEFAULT']['AutoResizeWindow'] == 'True'

    def set_auto_resize_window(self, value):
        if value == True:
            self.__config['DEFAULT']['AutoResizeWindow'] = 'True'
        else:
            self.__config['DEFAULT']['AutoResizeWindow'] = 'False'
        return self

    def get_comm_port(self):
        return self.__config['DEFAULT']['CommPort']

    def set_comm_port(self, value):
        self.__config['DEFAULT']['CommPort'] = value
        return self

    def get_entry_site_url(self):
        return self.__config['DEFAULT']['EntrySiteUrl']

    def set_entry_site_url(self, value):
        self.__config['DEFAULT']['EntrySiteUrl'] = value
        return self

    def get_entry_site_username(self):
        return self.__config['DEFAULT']['EntrySiteUsername']

    def set_entry_site_username(self,value):
        self.__config['DEFAULT']['EntrySiteUsername'] = value
        return self

    def get_entry_site_password(self):
        return self.__config['DEFAULT']['EntrySitePassword']

    def set_entry_site_password(self,value):
        self.__config['DEFAULT']['EntrySitePassword'] = value
        return self

