from unittest import TestCase
from game import opponent_below_level_three


class TestOpponentBelowLevelThree(TestCase):

    def test_opponent_below_level_three_case_level_one(self):
        opponent = {'Name': 'A', 'Required Level': 1}
        expected = True
        actual = opponent_below_level_three(opponent)
        self.assertEqual(expected, actual)

    def test_opponent_below_level_three_case_level_two(self):
        opponent = {'Name': 'A', 'Required Level': 2}
        expected = True
        actual = opponent_below_level_three(opponent)
        self.assertEqual(expected, actual)

    def test_opponent_below_level_three_case_level_three(self):
        opponent = {'Name': 'A', 'Required Level': 3}
        expected = False
        actual = opponent_below_level_three(opponent)
        self.assertEqual(expected, actual)

    def test_opponent_below_level_three_case_level_four(self):
        opponent = {'Name': 'A', 'Required Level': 4}
        expected = False
        actual = opponent_below_level_three(opponent)
        self.assertEqual(expected, actual)
