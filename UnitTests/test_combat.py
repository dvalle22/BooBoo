import io
from unittest import TestCase
from unittest.mock import patch
from game import combat


class TestCombat(TestCase):

    @patch('builtins.input', return_value='1')
    @patch('game.combat_round', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_user_wants_another_round(self, mock_output, _, __):
        character = {'Level': 1, 'Current HP': 200, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        expected_output = 'Do you want to continue battling?'
        combat(character, opponent)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=18)
    @patch('builtins.input', return_value='1')
    @patch('game.combat_round', return_value=True)
    def test_combat_opponent_flees_after_round(self, _, __, ___):
        character = {'Level': 1, 'Current HP': 100, 'Current XP': 2,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        expected = False
        actual = combat(character, opponent)
        self.assertEqual(expected, actual)
        self.assertEqual(opponent['isScared'], True)

    @patch('builtins.input', return_value='2')
    @patch('game.combat_round', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_user_flees_right_away(self, mock_output, _, __):
        character = {'Level': 2, 'Current HP': 200, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        expected_return = False
        actual_return = combat(character, opponent)
        unexpected_output = 'Do you want to continue battling?'
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expected_return, actual_return)
        self.assertFalse(unexpected_output in the_game_printed_this)

    @patch('random.randint', return_value=90)
    @patch('builtins.input', return_value='1')
    def test_combat_opponent_defeated_after_round(self, _, __):
        character = {'Level': 2, 'Current HP': 200, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 6, 'Damage': 50, 'Accuracy': 95}}
        opponent = {'Name': 'An auditionee girlie', 'Damage': 6, 'Current HP': 50, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        expected_return = True
        actual_return = combat(character, opponent)
        self.assertEqual(expected_return, actual_return)

    @patch('random.randint', return_value=90)
    @patch('builtins.input', return_value='1')
    def test_combat_character_defeated_after_round(self, _, __):
        character = {'Level': 2, 'Current HP': 5, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 6, 'Damage': 50, 'Accuracy': 95}}
        opponent = {'Name': 'An auditionee girlie', 'Damage': 6, 'Current HP': 200, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 95}
        expected_return = False
        actual_return = combat(character, opponent)
        self.assertEqual(expected_return, actual_return)

    @patch('builtins.input', return_value='1')
    @patch('game.combat_round', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_opponent_name_displayed(self, mock_output, _, __):
        character = {'Level': 1, 'Current HP': 200, 'Current XP': 2,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 300, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        expected_output = 'An auditionee girlie challenges you along the way!'
        combat(character, opponent)
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
