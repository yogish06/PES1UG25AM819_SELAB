import pytest
from bowling_alley import lane_cost, frame_score, lane_assignment


# ---- given examples ----
def test_weekday_booking():
    assert lane_cost("weekday", 2, 4, 2, False) == 900

def test_open_frame():
    assert frame_score(3, 4, []) == 7


# ---- lane_cost ----
def test_weekend_large_group_league():
    # 600*2 + 100*2 + 3*50 = 1550 ; 1550 - 310 = 1240
    assert lane_cost("weekend", 2, 6, 3, True) == 1240

def test_unknown_day_type():
    with pytest.raises(ValueError, match="unknown day type"):
        lane_cost("holiday", 1, 2, 0, False)

def test_invalid_booking():
    with pytest.raises(ValueError, match="invalid booking"):
        lane_cost("weekday", 0, 2, 0, False)

def test_too_many_shoe_rentals():
    with pytest.raises(ValueError, match="too many shoe rentals"):
        lane_cost("weekday", 1, 2, 3, False)


# ---- frame_score ----
def test_strike():
    assert frame_score(10, 0, [10, 10]) == 30

def test_spare():
    assert frame_score(5, 5, [3]) == 13

def test_invalid_roll():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(-1, 3, [])

def test_invalid_frame():
    with pytest.raises(ValueError, match="invalid frame"):
        frame_score(7, 5, [])


# ---- lane_assignment ----
def test_no_lanes_free():
    assert lane_assignment(4, False, 0) == "wait"

def test_kids_get_bumper_lane():
    assert lane_assignment(4, True, 3) == "bumper lane"

def test_big_group_two_lanes():
    assert lane_assignment(8, False, 2) == "two lanes"

def test_big_group_waits_for_lanes():
    assert lane_assignment(8, False, 1) == "wait"

def test_standard_lane():
    assert lane_assignment(4, False, 3) == "standard lane"
