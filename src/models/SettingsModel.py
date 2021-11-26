class SettingsModel(object):

    def __init__(self):
        pass

    def get_server_ip(self):
        return "192.168.0.10"

    def get_chipcontroll_interval(self):
        return 1000

    def get_chipcontroll_wait_after_read(self):
        return 1500

    def get_auto_maximize_opening_window(self):
        return False
