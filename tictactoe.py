from copy import deepcopy
from typing import NamedTuple, Optional

import constants as c


def main():
    """
    Runs a game of tic-tac-toe. Asks players "X" and "O" to alternate choosing squares of the
    tic-tac-toe board to fill in. After each turn, will check the board to see if there is a winner.
    If all squares are filled but no winner is detected, will end and call it a tie-game.
    """
    # each square in the board is assigned a label (1a-3c)
    board_values = deepcopy(c.INITIAL_BOARD_VALUES)

    print_welcome_message(board_values)

    winner = None
    current_player = None
    while winner is None:
        # current player is either "X" or "O"
        current_player = get_next_player(current_player)

        # ask the current player to choose a square
        chosen_square = get_next_move(current_player, board_values)

        # update the board, show it, and check for a winner or a full board
        board_values[chosen_square] = current_player
        print_board(board_values)
        winner = get_winner(board_values)

    print(get_final_message(winner))


def print_welcome_message(board_values: dict[str, str]):
    """
    Prints a nice welcome message and displays the empty board.

    :param board_values: Map of current, empty board values. Empty squares should map to their
                         square label.
    """
    print(c.INTRO_MESSAGE)
    print_board(board_values)


def print_board(board_values: dict[str, str]):
    """
    Prints a diagram of the current tic-tac-toe board.

    :param board_values: Map of current board values. Empty squares should map to their square
                         label. Filled squares should map to either "X" or "O".
    """
    print(c.BOARD.format(**board_values))


def get_final_message(winner: str) -> str:
    """
    Displays the final message indicating the winner. If there is no winner but the board is full,
    will display a tie message.

    :param winner: "X", "O", or "Tie"
    """
    if winner == c.TIE:
        return c.TIE_MESSAGE
    else:
        return c.WINNER_MESSAGE.format(player=winner)


def get_next_player(current_player: Optional[str]) -> str:
    """
    Chooses the next player, based on the current one. If there is no current player, we'll start
    with X.

    :param current_player: "X", "O", or None
    :return: The next player (either "X" or "O")
    """
    if current_player == c.X:
        return c.O
    else:
        return c.X


def get_next_move(current_player: str, board_values: dict[str, str]) -> str:
    """
    Asks the current player to pick an empty square and returns their choice. If the player inputs
    an invalid choice, will print an invalid response message and ask again until valid input is
    received. Invalid choices include:
    - a value that doesn't map to a square label (1a-3c)
    - a square that has already been filled in by either player

    :param current_player: The player to request input for (either "X" or "O")
    :param board_values: Map from square label (1a-3c) to square's values (1a-3c for empty squares,
                         "X" or "O" for filled squares)
    :return: The current player's chosen square
    """
    valid_input = False
    while not valid_input:
        # take care of any excess whitespace around the input and converts to lowercase
        raw_input = input(c.NEXT_TURN_MESSAGE.format(player=current_player))

        validation_result = get_validation_result(raw_input, board_values)

        if not validation_result.is_valid:
            print(validation_result.error_message)
            continue

        return validation_result.cleaned_input


class ValidationResult(NamedTuple):
    """ Represents results of validations performed on a player's raw input during the game """
    is_valid: bool
    cleaned_input: str
    error_message: Optional[str]


def get_validation_result(raw_input: str, board_values: dict[str, str]) -> ValidationResult:
    """
    Removes excess whitespace around the input, converts to lowercase, and checks that the input is
    valid. Invalid choices include:
    - a value that doesn't map to a square label (1a-3c)
    - a square that has already been filled in by either player

    :param raw_input: Raw input from player
    :param board_values: Map from square label (1a-3c) to square's values (1a-3c for empty squares,
                         "X" or "O" for filled squares)
    :return: ValidationResult indicating whether the input was valid ("is_valid"), the cleaned
             input with whitespace removed/converted to lowercase ("cleaned_input"), and, if not
             valid, an error message explaining why the input did not pass validation
             ("error_message").
    """
    # take care of any excess whitespace around the input and convert to lowercase
    cleaned_input = raw_input.strip().lower()

    # check if the input is a valid value (1a-3c)
    if cleaned_input not in board_values.keys():
        return ValidationResult(is_valid=False,
                                cleaned_input=cleaned_input,
                                error_message=c.INVALID_SQUARE_MESSAGE.format(input=cleaned_input))

    # check if the input is a square that's already filled
    if board_values[cleaned_input] in [c.X, c.O]:
        return ValidationResult(is_valid=False,
                                cleaned_input=cleaned_input,
                                error_message=c.UNAVAILABLE_SQUARE_MESSAGE.format(
                                    square=cleaned_input))

    return ValidationResult(is_valid=True,
                            cleaned_input=cleaned_input,
                            error_message=None)


def get_winner(board_values: dict[str, str]) -> Optional[str]:
    """
    Checks the board values to see if a player has won by manually checking all possible
    combinations (horizontal lines, vertical lines, and two diagonals). A player has won a combo if
    all entries in the combo have the same value (either "X" or "O").

    :param board_values: Map from square label (1a-3c) to square's values (1a-3c for empty squares,
                         "X" or "O" for filled squares)
    :return: The winner of the game ("X" or "O")
    """
    for combo in c.WINNING_COMBOS:
        entries = {board_values[k] for k in combo}
        if len(entries) == 1:
            return entries.pop()

    # if all the squares are filled but no winners were detected, it's a tie
    if set(board_values.values()) == {c.X, c.O}:
        return c.TIE

    return None


if __name__ == "__main__":
    main()
