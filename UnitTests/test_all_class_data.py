from unittest import TestCase
from game import all_class_data


class TestAllClassData(TestCase):

    def test_all_class_data(self):
        expected = {"1": {'Name': 'JUMPER', 'Damage': 70, 'Max HP': 50, 'XP Cap': 20, 'Accuracy': 30,
                          'Description': 'Very light on your feet. A lot of power goes into making those jumps look '
                          '\neffortless!',
                          'Attack Name': 'SHOOTING GRAND JETE - You leap into a stunning split midair, gliding '
                          '\nforward and impaling your pointed foot right into the opponent!'},
                    "2": {'Name': 'TURNER', 'Damage': 50, 'Max HP': 100, 'XP Cap': 25, 'Accuracy': 50,
                          'Description': 'You spin like a top. ',
                          'Attack Name': 'TORNADO PIROUETTES - You rotate so fast that you produce a tornado headed '
                          '\nright for the opponent!'},
                    "3": {'Name': 'BENDER', 'Damage': 25, 'Max HP': 160, 'XP Cap': 25, 'Accuracy': 40,
                          'Description': 'Legs for days, honey. You got the lines that ballet enthusiasts gush over.',
                          'Attack Name': 'GRAND BATTEMENT SLAM - You kick your leg forward tapping your shoulder, '
                          '\nand then slamming it back down into the opponent!'},
                    "4": {'Name': 'EXPRESSER', 'Damage': 10, 'Max HP': 300, 'XP Cap': 10, 'Accuracy': 90,
                          'Description': 'You don\'t have strong technical abilities like the other classes, but you '
                                         'sell \nit in the face. You give the drama.',
                          'Attack Name': 'HEART TOUCHING EMOTION - You perform a cute little act. Your opponent so '
                                         '\ntransfixed that they question their own performance abilities in '
                                         'comparison!'}}
        actual = all_class_data()
        self.assertEqual(expected, actual)
