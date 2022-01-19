import io
from unittest import TestCase
from unittest.mock import patch
from game import gain_xp


class TestGainXP(TestCase):

    def test_gain_xp_below_cap(self):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 2,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        gain_xp(character, opponent)
        expected_character = {'Level': 1, 'Current HP': 25, 'Current XP': 7,
                              'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        self.assertEqual(expected_character, character)

    def test_gain_xp_character_starts_at_zero(self):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 0,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        gain_xp(character, opponent)
        expected_character = {'Level': 1, 'Current HP': 25, 'Current XP': 5,
                              'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_xp_below_cap_output(self, mock_output):
        character = {'Level': 1, 'Current HP': 20, 'Current XP': 2,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        expected_output = '\nYou gained 5XP!' \
                          '\n\nYou are now at a current XP of 7.\n'
        gain_xp(character, opponent)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_xp_reached_cap(self, mock_output):
        character = {'Level': 1, 'Current HP': 20, 'Current XP': 5,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        expected_output = 'You are now at a current XP of 0.'
        gain_xp(character, opponent)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_xp_over_cap(self, mock_output):
        character = {'Level': 1, 'Current HP': 20, 'Current XP': 7,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        opponent = {'Name': 'An auditionee girlie', 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        expected_output = 'You are now at a current XP of 0.'
        gain_xp(character, opponent)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_gain_xp_opponent_unchanged(self):
        character = {'Level': 1, 'Current HP': 20, "Current XP": 2,
                     'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        gain_xp(character, opponent)
        self.assertEqual(opponent, {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5,
                                    'Required Level': 1, 'Accuracy': 10, 'isScared': False})
