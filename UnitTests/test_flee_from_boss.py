import io
from unittest import TestCase
from unittest.mock import patch
from game import flee_from_boss


class TestFleeFromBoss(TestCase):

    @patch('random.choice', return_value=20)
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_from_boss_lands_hit(self, mock_output, _, __):
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
        flee_from_boss(character, boss)
        expected_output = "Ouch! She got in one more hit before you could leave! You're down to 180HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 180)

    @patch('random.randint', return_value=21)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_from_boss_does_not_hit(self, mock_output, _):
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
        flee_from_boss(character, boss)
        expected_output = "You finally flee the scene..."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 200)

    @patch('random.choice', return_value=20)
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_from_boss_hits_character_hp_goes_to_zero(self, mock_output, _, __):
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
        flee_from_boss(character, boss)
        expected_output = "Ouch! She got in one more hit before you could leave! You're down to 0HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 0)

    @patch('random.choice', return_value=20)
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_from_boss_hits_character_hp_less_than_damage(self, mock_output, _, __):
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
        flee_from_boss(character, boss)
        expected_output = "Ouch! She got in one more hit before you could leave! You're down to 0HP."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
        self.assertEqual(character['Current HP'], 0)

    def test_flee_from_boss_unchanged_boss(self):
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
        flee_from_boss(character, boss)
        self.assertEqual(boss,
                         {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
                          'Accuracy': 90,
                          'Attack 1': {'Damage': 30,
                                       'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet "
                                               "pointe \nshoes at you! They may be worn out from all her performances, "
                                               "but they \nstill pack a punch!"},
                          'Attack 2': {'Damage': 20,
                                       'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}})
