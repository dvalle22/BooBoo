from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):

    @patch('random.choice', return_value='a lobby area. Nice and spacious.')
    def test_make_board_min_rows_and_columns(self, _):
        rows = 2
        columns = 2
        expected = {(0, 0): "\nYou enter the grand foyer of BunBun Ballet Academy. It's mesmerizing, what "
                            "\nyou've always dreamed of.",
                    (0, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 1): "\nYou enter a lobby area. Nice and spacious."}
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='a lobby area. Nice and spacious.')
    def test_make_board_min_rows(self, _):
        rows = 2
        columns = 4
        expected = {(0, 0): "\nYou enter the grand foyer of BunBun Ballet Academy. It's mesmerizing, what "
                            "\nyou've always dreamed of.",
                    (0, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (2, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (2, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (3, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (3, 1): "\nYou enter a lobby area. Nice and spacious."}
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='a lobby area. Nice and spacious.')
    def test_make_board_min_columns(self, _):
        rows = 4
        columns = 2
        expected = {(0, 0): "\nYou enter the grand foyer of BunBun Ballet Academy. It's mesmerizing, what "
                            "\nyou've always dreamed of.",
                    (0, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (0, 2): "\nYou enter a lobby area. Nice and spacious.",
                    (0, 3): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 2): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 3): "\nYou enter a lobby area. Nice and spacious."}
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='a lobby area. Nice and spacious.')
    def test_make_board_square_greater_than_min(self, _):
        rows = 4
        columns = 4
        expected = {(0, 0): "\nYou enter the grand foyer of BunBun Ballet Academy. It's mesmerizing, what "
                            "\nyou've always dreamed of.",
                    (0, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (0, 2): "\nYou enter a lobby area. Nice and spacious.",
                    (0, 3): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 2): "\nYou enter a lobby area. Nice and spacious.",
                    (1, 3): "\nYou enter a lobby area. Nice and spacious.",
                    (2, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (2, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (2, 2): "\nYou enter a lobby area. Nice and spacious.",
                    (2, 3): "\nYou enter a lobby area. Nice and spacious.",
                    (3, 0): "\nYou enter a lobby area. Nice and spacious.",
                    (3, 1): "\nYou enter a lobby area. Nice and spacious.",
                    (3, 2): "\nYou enter a lobby area. Nice and spacious.",
                    (3, 3): "\nYou enter a lobby area. Nice and spacious."}
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)
