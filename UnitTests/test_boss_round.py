import io
from unittest import TestCase
from unittest.mock import patch
from game import boss_round


class TestBossRound(TestCase):

    @patch('random.randint', return_value=100)
    def test_boss_round_both_alive(self, _):
        character = {'Level': 1, 'Current HP': 200, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        boss = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
                'Accuracy': 90,
                'Attack 1': {'Damage': 30,
                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                     "\nshoes at you! They may be worn out from all her performances, but they "
                                     "\nstill pack a punch!"},
                'Attack 2': {'Damage': 20,
                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        current_attack = {'Damage': 20,
                          'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}
        expected = True
        actual = boss_round(character, boss, current_attack)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_round_boss_defeated(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 200, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        boss = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 50,
                'Accuracy': 90,
                'Attack 1': {'Damage': 30,
                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                     "\nshoes at you! They may be worn out from all her performances, but they "
                                     "\nstill pack a punch!"},
                'Attack 2': {'Damage': 20,
                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        current_attack = {'Damage': 20,
                          'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}
        expected = False
        actual = boss_round(character, boss, current_attack)
        expected_output = "You successfully defeated her!"
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertTrue(expected_output in the_game_printed_this)

    @patch('random.randint', return_value=1)
    def test_boss_round_character_defeated(self, _):
        character = {'Level': 1, 'Current HP': 20, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        boss = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 200,
                'Accuracy': 90,
                'Attack 1': {'Damage': 30,
                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                     "\nshoes at you! They may be worn out from all her performances, but they "
                                     "\nstill pack a punch!"},
                'Attack 2': {'Damage': 20,
                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        current_attack = {'Damage': 20,
                          'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}
        expected = False
        actual = boss_round(character, boss, current_attack)
        self.assertEqual(expected, actual)

    def test_combat_boss_attack_unchanged(self):
        character = {'Level': 1, 'Current HP': 200, 'Current XP': 7,
                     'Class': {'Attack Name': 'Bop', 'XP Cap': 10, 'Max HP': 40, 'Damage': 50, 'Accuracy': 30}}
        boss = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
                'Accuracy': 90,
                'Attack 1': {'Damage': 30,
                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                     "\nshoes at you! They may be worn out from all her performances, but they "
                                     "\nstill pack a punch!"},
                'Attack 2': {'Damage': 20,
                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        current_attack = {'Damage': 20,
                          'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}
        boss_round(character, boss, current_attack)
        self.assertEqual(current_attack, {'Damage': 20,
                                          'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"})

