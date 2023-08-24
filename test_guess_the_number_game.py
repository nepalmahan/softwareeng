import pytest
from unittest.mock import patch
from guess_the_number_game import play_game

# This function helps the user to mock the simulation of user input
def mock_input(prompt):
    if "Enter your guess:" in prompt:
        return "1234"
    elif "Do you want to quit? (y/n):" in prompt:
        return "y"

@pytest.mark.parametrize("mocked_input, expected_output", [
    ("1234\ny", None),  # Quit on first attempt
    ("5678\nn", None),  # Quit on first attempt
    ("1234\n", None),   # Correct guess in first attempt
])
def test_play_game(mocked_input, expected_output):
    with patch("builtins.input", side_effect=mock_input):
        result = play_game()
    assert result == expected_output
