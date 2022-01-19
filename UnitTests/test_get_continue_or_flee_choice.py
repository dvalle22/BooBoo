import io
from unittest import TestCase
from unittest.mock import patch
from game import get_continue_combat_or_flee_choice


class TestContinueOrFlee(TestCase):

    @patch('builtins.input', return_value='1')
    def test_get_continue_combat_or_flee_choice_is_continue(self, _):
        expected = '1'
        actual = get_continue_combat_or_flee_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_get_continue_combat_or_flee_choice_is_flee(self, _):
        expected = '2'
        actual = get_continue_combat_or_flee_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0', '3', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_continue_combat_or_flee_choice_out_of_range_inputs(self, mock_output, _):
        expected_return = '1'
        actual = get_continue_combat_or_flee_choice()
        expected_output = "\nInvalid selection!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(expected_return, actual)
