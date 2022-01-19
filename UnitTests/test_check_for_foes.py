from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckFoes(TestCase):

    @patch('random.randint', return_value=1)
    def test_check_for_foes_random_integer_is_one(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_check_for_foes_random_integer_is_two(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=20)
    def test_check_for_foes_random_integer_is_twenty(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=100)
    def test_check_for_foes_random_integer_is_one_hundred(self, _):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=21)
    def test_check_for_foes_random_integer_is_twenty_one(self, _):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)
