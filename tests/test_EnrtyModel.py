from src.models.EnrtyModel import EntryModel
def test_checkentry_restult():
    entry=EntryModel()
    response=[]
    assert entry.checkentryResult(response) == False
    response={'result': 200, 'response': {'firstname': 'Anita', 'lastname': 'Nagy', 'rfid': 'afdfa', 'distance': '10,5 km', 'startnum': '20002', 'payed': 1}}
    assert entry.checkentryResult(response) == True
