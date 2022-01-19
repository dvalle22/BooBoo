from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):

    def test_move_character_start_at_top_left_corner_move_south(self):
        character = {'X-position': 0, 'Y-position': 0, 'Current HP': 5}
        move_character(character, "SOUTH")
        self.assertEqual({'X-position': 0, 'Y-position': 1, 'Current HP': 5}, character)

    def test_move_character_start_at_top_left_corner_move_east(self):
        character = {'X-position': 0, 'Y-position': 0, 'Current HP': 5}
        move_character(character, "EAST")
        self.assertEqual({'X-position': 1, 'Y-position': 0, 'Current HP': 5}, character)

    def test_move_character_start_at_middle_of_board_corner_move_north(self):
        character = {'X-position': 24, 'Y-position': 24, 'Current HP': 5}
        move_character(character, "NORTH")
        self.assertEqual({'X-position': 24, 'Y-position': 23, 'Current HP': 5}, character)

    def test_move_character_start_at_middle_of_board_corner_move_west(self):
        character = {'X-position': 24, 'Y-position': 24, 'Current HP': 5}
        move_character(character, "WEST")
        self.assertEqual({'X-position': 23, 'Y-position': 24, 'Current HP': 5}, character)
