import io
from unittest import TestCase
from unittest.mock import patch
from game import flee_early


class TestFleeEarly(TestCase):

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_early_opponent_lands_hit(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 40, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 10, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        flee_early(character, opponent)
        expected_output = "Ouch! She got in one more hit before you could leave! " \
                          "You're down to 30HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 30)

    @patch('random.randint', return_value=21)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_early_opponent_does_not_hit(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 40, 'Current XP': 2,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 10, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        flee_early(character, opponent)
        expected_output = "You flee the scene..."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 40)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_early_opponent_hits_character_hp_goes_to_zero(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 10, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 10, 'Current HP': 80, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        flee_early(character, opponent)
        expected_output = "Ouch! She got in one more hit before you could leave! " \
                          "You're down to 0HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 0)

    @patch('random.randint', return_value=19)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_early_opponent_hits_character_hp_not_high_enough(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 9, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 10, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        flee_early(character, opponent)
        expected_output = "Ouch! She got in one more hit before you could leave! " \
                          "You're down to 0HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 0)

    @patch('random.randint', return_value=20)
    def test_flee_early_opponent_unchanged(self, _):
        character = {'Level': 1, 'Current HP': 40, 'Current XP': 5,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        opponent = {'Name': "An auditionee girlie", 'Damage': 10, 'Current HP': 100, 'XP worth': 5, 'Required Level': 1,
                    'Accuracy': 10, 'isScared': False}
        flee_early(character, opponent)
        self.assertEqual(opponent, {'Name': "An auditionee girlie", 'Damage': 10, 'Current HP': 100, 'XP worth': 5,
                                    'Required Level': 1, 'Accuracy': 10, 'isScared': False})
