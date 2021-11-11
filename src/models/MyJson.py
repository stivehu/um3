from json import loads


class MyJson(object):
    @staticmethod
    def loads(data):
        if MyJson.verifyJson(data):
            return loads(data)
        else:
            return None

    @staticmethod
    def verifyJson(data):
        try:
            loads(data)
        except (ValueError, TypeError) as e:
            return False
        return True
