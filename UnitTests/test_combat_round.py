import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_round


class TestCombatRound(TestCase):

    @patch('random.randint', return_value=100)
    def test_combat_round_both_alive(self, _):
        character = {'Level': 1, 'Current HP': 100, 'Current XP': 2,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        expected = True
        actual = combat_round(character, opponent)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_defeated(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 100, 'Current XP': 2,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 50, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        expected = False
        actual = combat_round(character, opponent)
        expected_output = "\nYou successfully defeated her!"
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=1)
    def test_combat_round_character_defeated(self, _):
        character = {'Level': 1, 'Current HP': 6, 'Current XP': 2,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 50, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        expected = False
        actual = combat_round(character, opponent)
        self.assertEqual(expected, actual)
