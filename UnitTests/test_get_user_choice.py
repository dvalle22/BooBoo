import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):

    @patch('builtins.input', return_value='2')
    def test_get_user_choice_acceptable_input(self, _):
        expected = 'SOUTH'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='quit')
    def test_get_user_choice_quit_as_input(self, _):
        expected = 'quit'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_out_of_range_input_followed_by_acceptable(self, mock_output, _):
        expected_output = '\nStop playing around!'
        get_user_choice()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['QUIT', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_incorrect_case_followed_by_acceptable(self, mock_output, _):
        expected_output = '\nStop playing around!'
        get_user_choice()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['quit ', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_whitespace_input_followed_by_acceptable(self, mock_output, _):
        expected_output = '\nStop playing around!'
        get_user_choice()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_empty_input_followed_by_acceptable(self, mock_output, _):
        expected_output = '\nStop playing around!'
        get_user_choice()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
