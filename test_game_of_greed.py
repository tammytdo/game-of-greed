import pytest
from game_of_greed import make_choice
from game_of_greed import calculate_points
from game_of_greed import start_turn


# test_zilch
# non scoring roll should return 0
def test_zilch():
    assert calculate_points[2, 3, 4, 6] == 0
    assert calculate_points[] == 0

# test_ones
# rolls with various number of 1s should return correct score
def test_ones():
    assert [1,2,3,4,5,2] == 100
    assert calculate_points[1, 2, 3, 4, 6] == 100
    assert calculate_points[1] == 100



# test_twos
# rolls with various number of 2s should return correct score
def test_twos():
    assert calculate_points[2,2] == 0
    assert calculate_points[2,3,4] == 0
    assert calculate_points[2,2,2] == 200
    assert calculate_points[2,2,2,2] == 400


# test_threes
# rolls with various number of 3s should return correct score
def test_threes():
    assert calculate_points[3,3] == 0
    assert calculate_points[2,3,4] == 0
    assert calculate_points[3,3,3] == 300
    assert calculate_points[3,3,3,3] == 600

# test_fours
# rolls with various number of 4s should return correct score
def test_fours():
    assert calculate_points[4,4] == 0
    assert calculate_points[2,3,4] == 0
    assert calculate_points[4,4,4] == 400
    assert calculate_points[4,4,4,4,4,4] == 2400

# test_fives
# rolls with various number of 5s should return correct score
def test_fives():
    assert calculate_points[5,5] == 100
    assert calculate_points[2,3,5] == 50
    assert calculate_points[5,5,5] == 500
    assert calculate_points[5,5,5,5,5] == 2000

# test_sixes
# rolls with various number of 6s should return correct score
def test_sixes():
    assert calculate_points[6,6] == 0
    assert calculate_points[2,3,6] == 0
    assert calculate_points[1, 6, 6] == 100
    assert calculate_points[6, 6, 6, 6, 6, 6] == 3600

# test_straight
# 1,2,3,4,5,6 should return correct score
def test_straight():
    assert calculate_points[1, 2, 3, 4, 5, 6] == 1500
    assert calculate_points[1, 2, 3, 6, 5, 4] == 1500

# test_three_pairs
# 3 pairs should return correct score
def test_three_pairs():
    assert calculate_points[6,6,2,2,4,4] == 1500
    assert calculate_points[2,4,6,2,4,6] == 1500

# test_leftover_ones
# 1s not used in set of 3 (or greater) should return correct score
def test_leftover_ones():
    assert calculate_points[2,4,6,2,4,6] == 1500

# test_leftover_fives
# 5s not used in set of 3 (or greater) should return correct score
def test_leftover_fives():
    assert calculate_points[5, 2, 2, 2, 3, 4] == 250


# test_two_trios
# 2 sets of 3 should return correct score
def test_two_trios():
    assert calculate_points[2,2,2,3,3,3] == 500

# test_roll
# doing a roll with x number of dice should return sequence of x length random integers between 1 and 6 inclusive
def test_roll():
    start_turn()
    assert num_die_to_roll == 6

