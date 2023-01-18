from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(ValueError) as exp:
        Point(123, 12.4666, 10.667)
    assert str(exp.value) == "The name is not of String type"
    with pytest.raises(ValueError) as exp:
        Point("India", 12.4666, -200.667)
    assert str(exp.value) == "Invalid Latitude or Longitutde"
