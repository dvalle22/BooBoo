import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_your_turn


class TestCombatYourTurn(TestCase):

    @patch('random.randint', return_value=31)
    def test_combat_your_turn_opponent_dodged(self, _):
        character = {'Level': 1, 'Current HP': 15, 'Current XP': 8,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_your_turn(character, opponent)
        self.assertEqual(opponent, {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5,
                                    'Required Level': 1, 'Accuracy': 10, 'isScared': False})

    @patch('random.randint', return_value=100)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_your_turn_opponent_dodged_output(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 5, 'Current XP': 5,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 90, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_your_turn(character, opponent)
        expected_output = 'Darn, she dodged your attack!'
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=30)
    def test_combat_your_turn_opponent_land_hit(self, _):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 8,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_your_turn(character, opponent)
        self.assertEqual(opponent['Current HP'], 50)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_your_turn_opponent_land_hit_output(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 15, 'Current XP': 5,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 90, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_your_turn(character, opponent)
        expected_output = "Direct Hit! You deal 50 damage! \nThat brings her down to 40HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_combat_character_unchanged(self):
        character = {'Level': 1, 'Current HP': 25, 'Current XP': 12,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 0, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        combat_your_turn(character, opponent)
        self.assertEqual(character, {'Level': 1, 'Current HP': 25, 'Current XP': 12,
                                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50,
                                               'Accuracy': 30}})
