from unittest import TestCase
from game import all_foe_data


class TestAllFoeData(TestCase):
    def test_all_foe_data(self):
        expected = ({'Name': 'An auditionee girlie', 'Damage': 6, 'Current HP': 25, 'XP worth': 5, 'Required Level': 1,
                     'Accuracy': 10},
                    {'Name': 'An apprentice girlie', 'Damage': 9, 'Current HP': 30, 'XP worth': 5, 'Required Level': 1,
                     'Accuracy': 20},
                    {'Name': 'A corps girlie', 'Damage': 12, 'Current HP': 40, 'XP worth': 10, 'Required Level': 2,
                     'Accuracy': 30},
                    {'Name': "A soloist girlie, careful this one's a lot stronger than the others...", 'Damage': 15,
                     'Current HP': 60, 'XP worth': 20, 'Required Level': 3, 'Accuracy': 50})
        actual = all_foe_data()
        self.assertEqual(expected, actual)

