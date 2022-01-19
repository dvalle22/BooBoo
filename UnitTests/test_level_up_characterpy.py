import io
from unittest import TestCase
from unittest.mock import patch
from game import level_up_character


class TestLevelUp(TestCase):

    def test_level_up_character_start_level_one(self):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 12,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        level_up_character(character)
        expected_character = {'Level': 2, 'Current HP': 60, 'Current XP': 0,
                              'Class': {'XP Cap': 20, 'Max HP': 60, 'Damage': 60}}
        actual = character
        self.assertEqual(expected_character, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_character_start_level_one_output(self, mock_output):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 12,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        level_up_character(character)
        expected_output = ("\nCongratulations! You are now at level 2! "
                           "Your Max HP has increased to 60 and your attack damage has "
                           "increased to 60.")
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_level_up_character_start_level_two(self):
        character = {'Level': 2, 'Current HP': 60, 'Current XP': 25,
                     'Class': {'XP Cap': 20, 'Max HP': 60, 'Damage': 60}}
        level_up_character(character)
        expected_character = {'Level': 3, 'Current HP': 80, 'Current XP': 0,
                              'Class': {'XP Cap': 30, 'Max HP': 80, 'Damage': 70}}
        actual = character
        self.assertEqual(expected_character, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_character_start_level_two_output(self, mock_output):
        character = {'Level': 2, 'Current HP': 60, 'Current XP': 25,
                     'Class': {'XP Cap': 20, 'Max HP': 60, 'Damage': 60}}
        level_up_character(character)
        expected_output = ("\nCongratulations! You are now at level 3! "
                           "Your Max HP has increased to 80 and your attack damage has "
                           "increased to 70.")
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
