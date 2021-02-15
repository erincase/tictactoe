BOARD = """
      ||      || 
  {1a}  ||  {1b}  ||  {1c}
      ||      ||
======================
      ||      ||
  {2a}  ||  {2b}  ||  {2c}
      ||      ||
======================
      ||      ||
  {3a}  ||  {3b}  ||  {3c}
      ||      ||
"""

INITIAL_BOARD_VALUES = {"1a": "1a", "1b": "1b", "1c": "1c",
                        "2a": "2a", "2b": "2b", "2c": "2c",
                        "3a": "3a", "3b": "3b", "3c": "3c"}

WINNING_COMBOS = [
    ["1a", "1b", "1c"],
    ["2a", "2b", "2c"],
    ["3a", "3b", "3c"],
    ["1a", "2a", "3a"],
    ["1b", "2b", "3b"],
    ["3a", "3b", "3c"],
    ["1a", "2b", "3c"],
    ["1c", "2b", "3a"]
]

# player names - add an extra whitespace so it replaces a 2-character empty square value with a
# 2-character filled square value in the board above
X = "X "
O = "O "

TIE = "Tie"

INTRO_MESSAGE = "Welcome to tic-tac-toe!"

NEXT_TURN_MESSAGE = "Player {player}: Pick a square (1a-3c). "

INVALID_SQUARE_MESSAGE = "\"{input}\" is not a valid input. Please type an empty square value " \
                         "(1a-3c)."

UNAVAILABLE_SQUARE_MESSAGE = "Square {square} is already filled in. Please pick another square " \
                             "(1a-3c). "

WINNER_MESSAGE = "We have a winner - Player {player}! Great job!! \n"

TIE_MESSAGE = "Oops - Tie Game! No winners or losers here. :) \n"
