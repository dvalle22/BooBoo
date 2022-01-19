import io
from unittest import TestCase
from unittest.mock import patch
from game import combat_boss_turn


class TestCombatBossTurn(TestCase):

    @patch('random.randint', return_value=95)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_boss_turn_you_dodged(self, mock_output, _):
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
        combat_boss_turn(character, boss, current_attack)
        expected_output = "Woah you dodged her attack! Something tells you that's rare..."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 200)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_boss_turn_lands_hit(self, mock_output, _):
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
        combat_boss_turn(character, boss, current_attack)
        expected_output = "She got ya gal! OOF! You lose 20HP bringing you down to 180HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 180)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_boss_turn_lands_hit_character_down_to_zero_hp(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 20, 'Current XP': 7,
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
        combat_boss_turn(character, boss, current_attack)
        expected_output = "She got ya gal! OOF! You lose 20HP bringing you down to 0HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 0)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_boss_turn_lands_hit_hp_less_than_damage(self, mock_output, _):
        character = {'Level': 1, 'Current HP': 19, 'Current XP': 7,
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
        combat_boss_turn(character, boss, current_attack)
        expected_output = "She got ya gal! OOF! You lose 20HP bringing you down to 0HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 0)

    def test_combat_boss_and_attack_unchanged(self):
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
        combat_boss_turn(character, boss, current_attack)
        self.assertEqual(boss, {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24,
                                'Current HP': 300, 'Accuracy': 90,
                                'Attack 1': {'Damage': 30,
                                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old "
                                                     "ballet pointe \nshoes at you! They may be worn out from all her "
                                                     "performances, but they \nstill pack a punch!"},
                                'Attack 2': {'Damage': 20,
                                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}})
        self.assertEqual(current_attack, {'Damage': 20,
                                          'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"})
