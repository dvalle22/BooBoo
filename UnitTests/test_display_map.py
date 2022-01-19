import io
from unittest import TestCase
from unittest.mock import patch
from game import display_map


class TestDisplayMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_character_at_corner(self, mock_output):
        board = {(0, 0): 'empty', (0, 1): 'empty', (0, 2): 'empty', (0, 3): 'empty', (0, 4): 'empty',
                 (1, 0): 'empty', (1, 1): 'empty', (1, 2): 'empty', (1, 3): 'empty', (1, 4): 'empty',
                 (2, 0): 'empty', (2, 1): 'empty', (2, 2): 'empty', (2, 3): 'empty', (2, 4): 'empty',
                 (3, 0): 'empty', (3, 1): 'empty', (3, 2): 'empty', (3, 3): 'empty', (3, 4): 'empty',
                 (4, 0): 'empty', (4, 1): 'empty', (4, 2): 'empty', (4, 3): 'empty', (4, 4): 'empty'}
        character = {'X-position': 0, 'Y-position': 0}
        boss = {'X-position': 4, 'Y-position': 4}
        expected_output = "\n\n  ®    ®    ®    ®    ®  " \
                          "\n\n  ®    ®    ®    ®    ®  " \
                          "\n\n  ®    ®   [#]  [ ]  [ ] " \
                          "\n\n  ®    ®   [ ]  [ ]  [ ] " \
                          "\n\n  ®    ®   [ ]  [ ]  [ ] "
        display_map(board, character, boss)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_character_at_center(self, mock_output):
        board = {(0, 0): 'empty', (0, 1): 'empty', (0, 2): 'empty', (0, 3): 'empty', (0, 4): 'empty',
                 (1, 0): 'empty', (1, 1): 'empty', (1, 2): 'empty', (1, 3): 'empty', (1, 4): 'empty',
                 (2, 0): 'empty', (2, 1): 'empty', (2, 2): 'empty', (2, 3): 'empty', (2, 4): 'empty',
                 (3, 0): 'empty', (3, 1): 'empty', (3, 2): 'empty', (3, 3): "empty", (3, 4): 'empty',
                 (4, 0): 'empty', (4, 1): 'empty', (4, 2): 'empty', (4, 3): 'empty', (4, 4): 'empty'}
        character = {'X-position': 2, 'Y-position': 2}
        boss = {'X-position': 4, 'Y-position': 4}
        expected_output = "\n\n [ ]  [ ]  [ ]  [ ]  [ ] " \
                          "\n\n [ ]  [ ]  [ ]  [ ]  [ ] " \
                          "\n\n [ ]  [ ]  [#]  [ ]  [ ] " \
                          "\n\n [ ]  [ ]  [ ]  [ ]  [ ] " \
                          "\n\n [ ]  [ ]  [ ]  [ ]  [!] "
        display_map(board, character, boss)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_character_one_space_from_corner(self, mock_output):
        board = {(0, 0): 'empty', (0, 1): 'empty', (0, 2): 'empty', (0, 3): 'empty', (0, 4): 'empty',
                 (1, 0): 'empty', (1, 1): "empty", (1, 2): 'empty', (1, 3): 'empty', (1, 4): 'empty',
                 (2, 0): 'empty', (2, 1): 'empty', (2, 2): 'empty', (2, 3): 'empty', (2, 4): 'empty',
                 (3, 0): 'empty', (3, 1): 'empty', (3, 2): 'empty', (3, 3): 'empty', (3, 4): 'empty',
                 (4, 0): 'empty', (4, 1): 'empty', (4, 2): 'empty', (4, 3): 'empty', (4, 4): 'empty'}
        character = {'X-position': 3, 'Y-position': 1}
        boss = {'X-position': 4, 'Y-position': 4}
        expected_output = "\n\n  ®    ®    ®    ®    ®  " \
                          "\n\n [ ]  [ ]  [ ]  [ ]   ®  " \
                          "\n\n [ ]  [ ]  [#]  [ ]   ®  " \
                          "\n\n [ ]  [ ]  [ ]  [ ]   ®  " \
                          "\n\n [ ]  [ ]  [ ]  [ ]   ®  "
        display_map(board, character, boss)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_character_at_boss_location(self, mock_output):
        board = {(0, 0): 'empty', (0, 1): 'empty', (0, 2): 'empty', (0, 3): 'empty', (0, 4): 'empty',
                 (1, 0): 'empty', (1, 1): 'empty', (1, 2): 'empty', (1, 3): 'empty', (1, 4): 'empty',
                 (2, 0): 'empty', (2, 1): 'empty', (2, 2): "empty", (2, 3): 'empty', (2, 4): 'empty',
                 (3, 0): 'empty', (3, 1): 'empty', (3, 2): 'empty', (3, 3): 'empty', (3, 4): 'empty',
                 (4, 0): 'empty', (4, 1): 'empty', (4, 2): 'empty', (4, 3): 'empty', (4, 4): 'empty'}
        character = {'X-position': 4, 'Y-position': 4}
        boss = {'X-position': 4, 'Y-position': 4}
        expected_output = "\n\n [ ]  [ ]  [ ]   ®    ®  " \
                          "\n\n [ ]  [ ]  [ ]   ®    ®  " \
                          "\n\n [ ]  [ ]  [#]   ®    ®  " \
                          "\n\n  ®    ®    ®    ®    ®  " \
                          "\n\n  ®    ®    ®    ®    ®  "
        display_map(board, character, boss)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_display_map_all_arguments_unchanged(self):
        board = {(0, 0): '1', (0, 1): '2', (0, 2): '3', (0, 3): '4', (0, 4): '5',
                 (1, 0): '6', (1, 1): '7', (1, 2): '8', (1, 3): '9', (1, 4): '0',
                 (2, 0): 'A', (2, 1): 'B', (2, 2): 'C', (2, 3): 'D', (2, 4): 'E',
                 (3, 0): 'F', (3, 1): 'G', (3, 2): 'H', (3, 3): 'I', (3, 4): 'J',
                 (4, 0): 'K', (4, 1): 'L', (4, 2): 'M', (4, 3): 'N', (4, 4): 'O'}
        character = {'X-position': 4, 'Y-position': 4}
        boss = {'X-position': 4, 'Y-position': 4}
        display_map(board, character, boss)
        self.assertEqual(board, {(0, 0): "1", (0, 1): '2', (0, 2): '3', (0, 3): '4', (0, 4): '5',
                                 (1, 0): '6', (1, 1): '7', (1, 2): '8', (1, 3): '9', (1, 4): '0',
                                 (2, 0): 'A', (2, 1): 'B', (2, 2): 'C', (2, 3): 'D', (2, 4): 'E',
                                 (3, 0): 'F', (3, 1): 'G', (3, 2): 'H', (3, 3): 'I', (3, 4): 'J',
                                 (4, 0): 'K', (4, 1): 'L', (4, 2): 'M', (4, 3): 'N', (4, 4): 'O'})
        self.assertEqual(character, {'X-position': 4, 'Y-position': 4})
        self.assertEqual(boss, {'X-position': 4, 'Y-position': 4})
