import io
from unittest import TestCase
from unittest.mock import patch
from game import choose_class


class TestChooseClass(TestCase):

    @patch('builtins.input', side_effect='1')
    def test_choose_class_an_acceptable_input(self, _):
        expected = {'Name': 'JUMPER', 'Damage': 70, 'Max HP': 50, 'XP Cap': 20, 'Accuracy': 30,
                    'Description': 'Very light on your feet. A lot of power goes into making those jumps look '
                                   '\neffortless!',
                    'Attack Name': 'SHOOTING GRAND JETE - You leap into a stunning split midair, gliding '
                                   '\nforward and impaling your pointed foot right into the opponent!'}
        actual = choose_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_alphabetic_input_followed_by_acceptable(self, mock_output, __):
        choose_class()
        expected_output = "\nThat's not allowed!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=[' 3', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_whitespace_in_input_followed_by_acceptable(self, mock_output, __):
        choose_class()
        expected_output = "\nThat's not allowed!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_empty_input_followed_by_acceptable(self, mock_output, __):
        choose_class()
        expected_output = "\nThat's not allowed!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('builtins.input', side_effect=['5', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_numeric_out_of_range_followed_by_acceptable(self, mock_output, __):
        choose_class()
        expected_output = "\nThat's not allowed!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
