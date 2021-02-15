import unittest
from copy import deepcopy

import constants as c
import tictactoe as undertest
from tictactoe import ValidationResult


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.DEFAULT_BOARD = deepcopy(c.INITIAL_BOARD_VALUES)

    def test_get_next_player__first_move(self):
        """ If there is no first player, return player X """
        returned = undertest.get_next_player(None)
        expected = c.X
        self.assertEqual(expected, returned)

    def test_get_next_player__current_player_O(self):
        """ If the current player is O, return player X """
        returned = undertest.get_next_player(c.O)
        expected = c.X
        self.assertEqual(expected, returned)

    def test_get_next_player__current_player_X(self):
        """ If the current player is X, return player O """
        returned = undertest.get_next_player(c.X)
        expected = c.O
        self.assertEqual(expected, returned)

    def test_get_validation_result__strips_whitespace(self):
        """ Confirm we appropriately strip excess whitespace around raw input """
        raw_input = "     1a          "
        returned = undertest.get_validation_result(raw_input, self.DEFAULT_BOARD)
        expected = ValidationResult(is_valid=True,
                                    cleaned_input="1a",
                                    error_message=None)
        self.assertEqual(expected, returned)

    def test_get_validation_result__convert_to_lowercase(self):
        """ Confirm we convert input to lowercase """
        raw_input = "2B"
        returned = undertest.get_validation_result(raw_input, self.DEFAULT_BOARD)
        expected = ValidationResult(is_valid=True,
                                    cleaned_input="2b",
                                    error_message=None)
        self.assertEqual(expected, returned)

    def test_get_validation_result__invalid_square_value(self):
        """ Confirm we return the appropriate error message when user selects an invalid square """
        raw_input = "5c"
        returned = undertest.get_validation_result(raw_input, self.DEFAULT_BOARD)
        expected = ValidationResult(is_valid=False,
                                    cleaned_input="5c",
                                    error_message=c.INVALID_SQUARE_MESSAGE.format(input="5c"))
        self.assertEqual(expected, returned)

    def test_get_validation_result__filled_square_value(self):
        """ Confirm we return the appropriate error message when user selects a filled square """
        raw_input = "1a"
        board_values = self.DEFAULT_BOARD
        board_values[raw_input] = c.X

        returned = undertest.get_validation_result(raw_input, board_values)
        expected = ValidationResult(is_valid=False,
                                    cleaned_input="1a",
                                    error_message=c.UNAVAILABLE_SQUARE_MESSAGE.format(square="1a"))
        self.assertEqual(expected, returned)

    def test_get_winner__no_winner(self):
        """ Confirm we don't return a winner for an empty board """
        returned = undertest.get_winner(self.DEFAULT_BOARD)
        expected = None
        self.assertEqual(expected, returned)

    def test_get_winner__tie(self):
        """
        Confirm we detect a tie-game (filled board with no winners)
              ||      ||
          X   ||  X   ||  O
              ||      ||
        ======================
              ||      ||
          O   ||  O   ||  X
              ||      ||
        ======================
              ||      ||
          X   ||  X   ||  O
              ||      ||
        """
        board_values = {"1a": c.X, "1b": c.X, "1c": c.O,
                        "2a": c.O, "2b": c.O, "2c": c.X,
                        "3a": c.X, "3b": c.X, "3c": c.O}
        returned = undertest.get_winner(board_values)
        expected = c.TIE
        self.assertEqual(expected, returned)

    def test_get_winner__winner_X(self):
        """
        Confirm we detect the correct winner
              ||      ||
          X   ||  X   ||  X
              ||      ||
        ======================
              ||      ||
          O   ||  O   ||  2c
              ||      ||
        ======================
              ||      ||
          3a  ||  3b  ||  3c
              ||      ||
        """
        board_values = {"1a": c.X,  "1b": c.X,  "1c": c.X,
                        "2a": c.O,  "2b": c.O,  "2c": "2c",
                        "3a": "3a", "3b": "3b", "3c": "3c"}
        returned = undertest.get_winner(board_values)
        expected = c.X
        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()
