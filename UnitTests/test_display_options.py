import io
from unittest import TestCase
from unittest.mock import patch
from game import display_options


class TestDisplayOptions(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_options_one_item(self, mock_output):
        options_list = {'1': 'Hello'}
        expected_output = '1: Hello'
        display_options(options_list)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_options_two_items(self, mock_output):
        options_list = {'B': 'OK', 'A': 'NOPE'}
        expected_output = 'B: OK\n' \
                          'A: NOPE'
        display_options(options_list)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_options_more_than_two_items(self, mock_output):
        options_list = {'X': 'OK', 'Y': 'NOPE', 'Z': 'YUPP'}
        expected_output = 'X: OK\n' \
                          'Y: NOPE\n' \
                          'Z: YUPP'
        display_options(options_list)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_options_mixed_types_in_argument(self, mock_output):
        options_list = {20: 4, 'Y': 7.8, 11: 'ok'}
        expected_output = '20: 4\n' \
                          'Y: 7.8\n' \
                          '11: ok'
        display_options(options_list)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_display_options_argument_unchanged(self):
        options_list = {'B': 'OK', 'A': 'NOPE'}
        display_options(options_list)
        self.assertEqual(options_list, {'B': 'OK', 'A': 'NOPE'})
