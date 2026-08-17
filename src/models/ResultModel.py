from src.models.RemoteApiModel import RemoteApiModel


class ResultModel(object):

    def __init__(self):
        self.__remoteApi = RemoteApiModel()

    def get_result_url(self):
        return self.__remoteApi.get_result_url()

    def get_scoreboard_url(self, rfid):
        return self.__remoteApi.get_scoreboard_url(rfid)
