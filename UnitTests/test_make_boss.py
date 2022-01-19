from unittest import TestCase
from game import make_boss


class TestMakeBoss(TestCase):

    def test_make_boss(self):
        expected = {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
                    'Accuracy': 90,
                    'Attack 1': {'Damage': 30,
                                 'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                 "\nshoes at you! They may be worn out from all her performances, but they "
                                 "\nstill pack a punch!"},
                    'Attack 2': {'Damage': 20,
                                 'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}}
        actual = make_boss()
        self.assertEqual(expected, actual)
