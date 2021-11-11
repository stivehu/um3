entries_pickedup = '{  "startnum": "100",  "distance": "10 km",  "firstname": "Teszt",  "lastname": "Elek",  "gender": "Nő",  "gender_id": "2",  "agegroup": "7-15 Év",  "pickedUp": "True",  "pickedupstate": "Felvette"}'
entries_pickeddown = '{  "startnum": "100",  "distance": "10 km",  "firstname": "Teszt",  "lastname": "Elek",  "gender": "Nő", "gender_id": "2", "agegroup": "7-15 Év",  "pickedUp": "True",  "pickedupstate": "Felvette"}'
entries_badformat = '  startnum": "100",  "distance": "10 km",  "firstname": "Teszt",  "lastname": "Elek",  "gender": "Nő","gender_id": "2",  "agegroup": "7-15 Év",  "pickedUp": "True",  "pickedupstate": "Felvette"}'

distances = [{"id": 2, "name": "7-10 év", "groupedheader_id": 2, "minage": 7, "maxage": 10, "sortid": 1},
             {"id": 3, "name": "11-14 év", "groupedheader_id": 2, "minage": 11, "maxage": 14, "sortid": 2},
             {"id": 5, "name": "51-60 év", "groupedheader_id": 2, "minage": 51, "maxage": 60, "sortid": 7},
             {"id": 6, "name": "31-40 év", "groupedheader_id": 2, "minage": 31, "maxage": 40, "sortid": 5},
             {"id": 7, "name": "41-50 év", "groupedheader_id": 2, "minage": 41, "maxage": 50, "sortid": 6},
             {"id": 8, "name": "19-30 év", "groupedheader_id": 2, "minage": 19, "maxage": 30, "sortid": 4},
             {"id": 9, "name": "61 év felettiek", "groupedheader_id": 2, "minage": 61, "maxage": 150, "sortid": 8},
             {"id": 10, "name": "15-18 év", "groupedheader_id": 2, "minage": 15, "maxage": 18, "sortid": 3}]
entry_save_result = {
    'birthsday': '1978-02-08', 'category0_id': '5', 'category1_id': '7', 'category2_id': None, 'category3_id': None,
    'category4_id': None, 'category5_id': None, 'category6_id': None, 'category7_id': None, 'category8_id': None,
    'category9_id': None, 'distance_id': '5', 'firstname': 'Elek', 'lastname': 'Teszt', 'rfid': 'ABG3652AE',
    'settlement': 'Békéscsaba', 'startnum': '100'}

