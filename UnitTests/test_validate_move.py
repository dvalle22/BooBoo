from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):

    def test_validate_move_destination_in_board(self):
        board = {(0, 0): 'Empty', (0, 1): 'Empty', (1, 0): 'Empty', (1, 1): 'Empty'}
        character = {'X-position': 0, 'Y-position': 0, 'Current HP': 5}
        direction = 'EAST'
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_at_left_bound_destination_to_left(self):
        board = {(0, 0): 'Empty', (0, 1): 'Empty', (0, 2): 'Empty',
                 (1, 0): 'Empty', (1, 1): 'Empty', (1, 2): 'Empty',
                 (2, 0): 'Empty', (2, 1): 'Empty', (2, 2): 'Empty'}
        character = {'X-position': 0, 'Y-position': 1, 'Current HP': 5}
        direction = 'WEST'
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_at_right_bound_destination_to_right(self):
        board = {(0, 0): "Empty", (0, 1): 'Empty', (0, 2): 'Empty',
                 (1, 0): 'Empty', (1, 1): 'Empty', (1, 2): 'Empty',
                 (2, 0): 'Empty', (2, 1): 'Empty', (2, 2): 'Empty'}
        character = {'X-position': 2, 'Y-position': 2, 'Current HP': 5}
        direction = 'EAST'
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_at_top_bound_destination_up(self):
        board = {(0, 0): 'Empty', (0, 1): 'Empty', (0, 2): 'Empty',
                 (1, 0): 'Empty', (1, 1): "Empty", (1, 2): 'Empty',
                 (2, 0): 'Empty', (2, 1): 'Empty', (2, 2): 'Empty'}
        character = {'X-position': 1, 'Y-position': 0, 'Current HP': 5}
        direction = 'NORTH'
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_character_at_bottom_bound_destination_down(self):
        board = {(0, 0): 'Empty', (0, 1): 'Empty', (0, 2): 'Empty',
                 (1, 0): 'Empty', (1, 1): 'Empty', (1, 2): 'Empty',
                 (2, 0): 'Empty', (2, 1): 'Empty', (2, 2): "Empty"}
        character = {'X-position': 0, 'Y-position': 2, 'Current HP': 5}
        direction = 'SOUTH'
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_board_and_character_unchanged(self):
        board = {(0, 0): 'Empty', (0, 1): 'Empty', (0, 2): 'Empty',
                 (1, 0): 'Empty', (1, 1): 'Empty', (1, 2): "Empty",
                 (2, 0): 'Empty', (2, 1): 'Empty', (2, 2): "Empty"}
        character = {'X-position': 1, 'Y-position': 1, 'Current HP': 5}
        direction = 'WEST'
        validate_move(board, character, direction)
        self.assertEqual(board, {(0, 0): "Empty", (0, 1): 'Empty', (0, 2): 'Empty',
                                 (1, 0): "Empty", (1, 1): 'Empty', (1, 2): "Empty",
                                 (2, 0): 'Empty', (2, 1): 'Empty', (2, 2): "Empty"})
        self.assertEqual(character, {'X-position': 1, 'Y-position': 1, 'Current HP': 5})
