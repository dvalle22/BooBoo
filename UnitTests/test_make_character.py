from unittest import TestCase
from unittest.mock import patch
from game import make_character


class Test(TestCase):

    @patch('game.choose_class',
           return_value={'Name': 'TURNER', 'Damage': 50, 'Max HP': 100, 'XP Cap': 25,
                                 'Accuracy': 50, 'Description': 'You spin like a top. ',
                                 'Attack Name': 'TORNADO PIROUETTES - You rotate so fast that you produce a '
                                                'tornado headed \nright for the opponent!'})
    @patch('game.choose_name', return_value='Booboo')
    def test_make_character(self, _, __):
        expected = {'Name': 'Booboo', 'X-position': 0, 'Y-position': 0, 'Level': 1, 'Current XP': 0,
                    'Current HP': 100,
                    'Class': {'Name': 'TURNER', 'Damage': 50, 'Max HP': 100, 'XP Cap': 25,
                              'Accuracy': 50, 'Description': 'You spin like a top. ',
                              'Attack Name': 'TORNADO PIROUETTES - You rotate so fast that you produce a '
                                             'tornado headed \nright for the opponent!'}}
        actual = make_character()
        self.assertEqual(expected, actual)
