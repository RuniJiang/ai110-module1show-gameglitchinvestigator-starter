from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_too_high_guess_tells_player_to_go_lower():
    # Regression: hints were reversed ("Too High" said "Go HIGHER!")
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_guess_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_check_guess_compares_numerically_not_as_strings():
    # Regression: app.py passed the secret as a str on even attempts, which
    # made comparisons lexicographic ("9" > "50"). Ints must compare as ints.
    assert check_guess(9, 50)[0] == "Too Low"
    assert check_guess(100, 99)[0] == "Too High"
