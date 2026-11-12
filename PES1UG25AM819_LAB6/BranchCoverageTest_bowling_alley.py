import pytest
from bowling_alley import lane_cost, frame_score, lane_assignment


# ---- given examples ----
def test_weekday_booking():
    assert lane_cost("weekday", 2, 4, 2, False) == 900

def test_open_frame():
    assert frame_score(3, 4, []) == 7


# ---- lane_cost: every decision both ways ----
def test_weekend_large_group_league():
    assert lane_cost("weekend", 2, 6, 3, True) == 1240

def test_weekend_single_game_five_players():
    assert lane_cost("weekend", 1, 5, 0, False) == 700

def test_weekday_five_players():
    assert lane_cost("weekday", 1, 5, 0, False) == 500

def test_four_players_no_surcharge():
    assert lane_cost("weekday", 1, 4, 0, False) == 400

def test_league_member_discount():
    assert lane_cost("weekday", 1, 2, 1, True) == 360

def test_league_discount_no_shoes():
    assert lane_cost("weekday", 1, 1, 0, True) == 320

def test_shoes_equal_players_allowed():
    assert lane_cost("weekday", 1, 3, 3, False) == 550

def test_unknown_day_type():
    with pytest.raises(ValueError, match="unknown day type"):
        lane_cost("holiday", 1, 2, 0, False)

def test_invalid_games_zero():
    with pytest.raises(ValueError, match="invalid booking"):
        lane_cost("weekday", 0, 2, 0, False)

def test_invalid_players_zero():
    with pytest.raises(ValueError, match="invalid booking"):
        lane_cost("weekday", 1, 0, 0, False)

def test_invalid_players_seven():
    with pytest.raises(ValueError, match="invalid booking"):
        lane_cost("weekday", 1, 7, 0, False)

def test_six_players_allowed():
    assert lane_cost("weekday", 1, 6, 0, False) == 500

def test_too_many_shoe_rentals():
    with pytest.raises(ValueError, match="too many shoe rentals"):
        lane_cost("weekday", 1, 2, 3, False)


# ---- frame_score ----
def test_strike():
    assert frame_score(10, 0, [10, 10]) == 30

def test_strike_with_open_bonus():
    assert frame_score(10, 0, [3, 4]) == 17

def test_spare():
    assert frame_score(5, 5, [3]) == 13

def test_spare_with_zero_first_roll():
    assert frame_score(0, 10, [5]) == 15

def test_gutter_frame():
    assert frame_score(0, 0, []) == 0

def test_invalid_roll_negative_first():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(-1, 3, [])

def test_invalid_roll_first_above_ten():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(11, 0, [])

def test_invalid_roll_negative_second():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(3, -1, [])

def test_invalid_frame_over_ten():
    with pytest.raises(ValueError, match="invalid frame"):
        frame_score(7, 5, [])

def test_frame_total_nine_is_open():
    assert frame_score(4, 5, []) == 9


# ---- lane_assignment ----
def test_no_lanes_free():
    assert lane_assignment(4, False, 0) == "wait"

def test_no_lanes_free_with_kids_still_waits():
    assert lane_assignment(4, True, 0) == "wait"

def test_kids_get_bumper_lane():
    assert lane_assignment(4, True, 3) == "bumper lane"

def test_big_group_two_lanes():
    assert lane_assignment(8, False, 2) == "two lanes"

def test_big_group_one_lane_waits():
    assert lane_assignment(8, False, 1) == "wait"

def test_six_players_standard_lane():
    assert lane_assignment(6, False, 1) == "standard lane"

def test_standard_lane():
    assert lane_assignment(4, False, 3) == "standard lane"
