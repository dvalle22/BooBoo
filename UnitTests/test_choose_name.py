import io
from unittest import TestCase
from unittest.mock import patch
from game import choose_name


class TestChooseName(TestCase):

    @patch('builtins.input', return_value='ab')
    def test_choose_name_minimum_acceptable_characters(self, _):
        expected = 'ab'
        actual = choose_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', 'AB'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_name_insufficient_characters_followed_by_acceptable(self, mock_output, _):
        expected_output = "\nThat's not allowed!"
        choose_name()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['', 'abC'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_name_empty_input_followed_by_acceptable(self, mock_output, _):
        expected_output = "\nThat's not allowed!"
        choose_name()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['ArianaGrande', 'AA'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_name_too_many_characters_followed_by_acceptable(self, mock_output, _):
        expected_output = "\nThat's not allowed!"
        choose_name()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['Mi mi', 'AA'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_name_whitespace_in_input_followed_by_acceptable(self, mock_output, _):
        expected_output = "\nThat's not allowed!"
        choose_name()
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
