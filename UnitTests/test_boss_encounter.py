import io
from unittest import TestCase
from unittest.mock import patch
from game import boss_encounter


class TestBossEncounter(TestCase):

    @patch('game.boss_combat', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_encounter_boss_defeated(self, mock_output, _):
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
        boss_encounter(character, boss)
        expected_output = "You've ruined Miss Prima's career... it's over for her!" \
                          "\n\nBOSS DEFEATED!"
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)
