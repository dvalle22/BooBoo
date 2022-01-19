import io
from unittest import TestCase
from unittest.mock import patch
from game import foe_encounter


class TestFoeEncounter(TestCase):

    @patch('game.combat', return_value=True)
    @patch('builtins.input', return_value='1')
    def test_foe_encounter_opponent_defeated(self, _, __):
        character = {'Level': 2, 'Current HP': 100, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 6, 'Damage': 50, 'Accuracy': 95}}
        opponent = {'Name': 'An auditionee girlie', 'Damage': 6, 'Current HP': 50, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        foe_encounter(character, opponent)
        self.assertEqual(character['Current XP'], 8)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_encounter_opponent_flees(self, mock_output, _, __):
        character = {'Level': 2, 'Current HP': 200, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 6, 'Damage': 50, 'Accuracy': 95}}
        opponent = {'Name': 'An auditionee girlie', 'Damage': 6, 'Current HP': 200, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        foe_encounter(character, opponent)
        expected_output = "Well, you actually can't attack her anymore 'cause she vanished."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_encounter_character_flees(self, mock_output, _, __):
        character = {'Level': 2, 'Current HP': 100, 'Current XP': 3,
                     'Class': {'Attack Name': "Bop", 'XP Cap': 10, 'Max HP': 6, 'Damage': 50, 'Accuracy': 95}}
        opponent = {'Name': 'An auditionee girlie', 'Damage': 10, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10}
        foe_encounter(character, opponent)
        expected_output = "Ouch! She got in one more hit before you could leave!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 90)
