import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location


class TestDescribeCurrentLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_character_top_left_corner(self, mock_output):
        board = {(0, 0): '11', (0, 1): '22', (0, 2): '33', (0, 3): '44', (0, 4): '55',
                 (1, 0): '66', (1, 1): '77', (1, 2): '88', (1, 3): '99', (1, 4): '01',
                 (2, 0): "AA", (2, 1): 'BB', (2, 2): 'CC', (2, 3): 'DD', (2, 4): 'EE',
                 (3, 0): 'FF', (3, 1): 'GG', (3, 2): 'HH', (3, 3): 'II', (3, 4): 'JJ',
                 (4, 0): 'KK', (4, 1): 'LL', (4, 2): 'MM', (4, 3): 'NN', (4, 4): 'OO'}
        character = {'X-position': 0, 'Y-position': 0}
        expected_output = '11'
        describe_current_location(board, character)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_character_bottom_right_corner(self, mock_output):
        board = {(0, 0): '11', (0, 1): '22', (0, 2): '33', (0, 3): '44', (0, 4): '55',
                 (1, 0): '66', (1, 1): '77', (1, 2): '88', (1, 3): '99', (1, 4): '01',
                 (2, 0): "AA", (2, 1): 'BB', (2, 2): 'CC', (2, 3): 'DD', (2, 4): 'EE',
                 (3, 0): 'FF', (3, 1): 'GG', (3, 2): "HH", (3, 3): 'II', (3, 4): 'JJ',
                 (4, 0): 'KK', (4, 1): 'LL', (4, 2): 'MM', (4, 3): 'NN', (4, 4): 'OO'}
        character = {'X-position': 4, 'Y-position': 4}
        expected_output = 'OO'
        describe_current_location(board, character)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_character_in_inner_board(self, mock_output):
        board = {(0, 0): '11', (0, 1): '22', (0, 2): '33', (0, 3): '44', (0, 4): '55',
                 (1, 0): '66', (1, 1): '77', (1, 2): '88', (1, 3): '99', (1, 4): '01',
                 (2, 0): "AA", (2, 1): 'BB', (2, 2): 'CC', (2, 3): 'DD', (2, 4): 'EE',
                 (3, 0): 'FF', (3, 1): 'GG', (3, 2): "HH", (3, 3): "II", (3, 4): 'JJ',
                 (4, 0): 'KK', (4, 1): 'LL', (4, 2): 'MM', (4, 3): 'NN', (4, 4): 'OO'}
        character = {'X-position': 2, 'Y-position': 1}
        expected_output = 'BB'
        describe_current_location(board, character)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_describe_current_location_all_arguments_unchanged(self):
        board = {(0, 0): '11', (0, 1): '22', (0, 2): '33', (0, 3): '44', (0, 4): "55",
                 (1, 0): '66', (1, 1): '77', (1, 2): '88', (1, 3): '99', (1, 4): '01',
                 (2, 0): "AA", (2, 1): 'BB', (2, 2): 'CC', (2, 3): 'DD', (2, 4): 'EE',
                 (3, 0): 'FF', (3, 1): 'GG', (3, 2): "HH", (3, 3): "II", (3, 4): 'JJ',
                 (4, 0): 'KK', (4, 1): 'LL', (4, 2): 'MM', (4, 3): 'NN', (4, 4): 'OO'}
        character = {'X-position': 3, 'Y-position': 2}
        describe_current_location(board, character)
        self.assertEqual(board, {(0, 0): '11', (0, 1): '22', (0, 2): '33', (0, 3): '44', (0, 4): '55',
                                 (1, 0): '66', (1, 1): '77', (1, 2): '88', (1, 3): '99', (1, 4): '01',
                                 (2, 0): "AA", (2, 1): 'BB', (2, 2): 'CC', (2, 3): 'DD', (2, 4): 'EE',
                                 (3, 0): 'FF', (3, 1): "GG", (3, 2): 'HH', (3, 3): "II", (3, 4): 'JJ',
                                 (4, 0): 'KK', (4, 1): 'LL', (4, 2): 'MM', (4, 3): 'NN', (4, 4): 'OO'})
        self.assertEqual(character, {'X-position': 3, 'Y-position': 2})
