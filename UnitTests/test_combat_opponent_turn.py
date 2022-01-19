import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_opponent_turn


class TestOpponentTurn(TestCase):

    @patch('random.randint', return_value=11)
    def test_combat_opponent_turn_you_dodged(self, _):
        character = {'Level': 1, 'Current HP': 15, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_opponent_turn(character, opponent)
        self.assertEqual(character['Current HP'], 15)

    @patch('random.randint', return_value=100)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_opponent_turn_you_dodged_output(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 5,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 90, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_opponent_turn(character, opponent)
        expected_output = 'You managed to dodge her attack!'
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=10)
    def test_combat_opponent_turn_land_hit(self, _):
        character = {'Level': 1, 'Current HP': 36, 'Current XP': 8,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_opponent_turn(character, opponent)
        self.assertEqual(character['Current HP'], 30)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_opponent_turn_land_hit_output(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 16, 'Current XP': 5,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 90, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_opponent_turn(character, opponent)
        expected_output = "\nShe got ya gal! You lose 6HP bringing you down " \
                          "to 10HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=5)
    def test_combat_opponent_unchanged(self, _):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 8,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 50, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_opponent_turn(character, opponent)
        self.assertEqual(opponent, {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5,
                                    'Required Level': 1, 'Accuracy': 10, 'isScared': False})
