import io
from unittest import TestCase
from unittest.mock import patch
from game import boss_intro_text


class TestBossIntroText(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_intro_text(self, mock_output):
        boss = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
                'Accuracy': 90,
                'Attack 1': {'Damage': 30,
                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                     "\nshoes at you! They may be worn out from all her performances, but they "
                                     "\nstill pack a punch!"},
                'Attack 2': {'Damage': 20,
                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        boss_intro_text(boss)
        expected_output = "It's Principal dancer, Miss Prima. " \
                          "\"HOW DARE YOU THINK YOU'RE WORTHY OF APPROACHING ME, YOU'RE GONNA REGRET THIS!\", " \
                          "she shouts."
        the_game_printed_this = mock_output.getvalue()
        self.assertTrue(expected_output in the_game_printed_this)

    def test_boss_intro_text_boss_unchanged(self):
        boss = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
                'Accuracy': 90,
                'Attack 1': {'Damage': 30,
                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                     "\nshoes at you! They may be worn out from all her performances, but they "
                                     "\nstill pack a punch!"},
                'Attack 2': {'Damage': 20,
                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        boss_intro_text(boss)
        self.assertEqual(boss, {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24,
                                'Current HP': 300, 'Accuracy': 90,
                                'Attack 1': {'Damage': 30,
                                             'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old "
                                                     "ballet pointe \nshoes at you! They may be worn out from all her "
                                                     "performances, but they \nstill pack a punch!"},
                                'Attack 2': {'Damage': 20,
                                             'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}})
