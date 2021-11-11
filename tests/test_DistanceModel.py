import datetime
from unittest.mock import patch, Mock

from src.models.DistanceModel import DistanceModel


def test_distance_model():
    distanceModel = DistanceModel()
    datetime_mock = Mock(wraps=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2020, 1, 1)
    with patch('datetime.datetime', new=datetime_mock):
        assert distanceModel.get_age_from_birthday('1978-02-05') == 42
        assert distanceModel.get_age_from_birthday('1900-02-05') == 120
