from unittest import TestCase
from game import generate_foe


class Test(TestCase):

    def test_generate_foe_character_level_one(self):
        character = {'Name': 'Oop', 'X-position': 0, 'Y-position': 0, 'Level': 1}
        expected_level_pool = [1, 2]
        foe = generate_foe(character)
        self.assertTrue(foe['Required Level'] in expected_level_pool)

    def test_generate_foe_character_level_two(self):
        character = {'Name': 'Oop', 'X-position': 0, 'Y-position': 0, 'Level': 2}
        expected_level_pool = [1, 2]
        foe = generate_foe(character)
        self.assertTrue(foe['Required Level'] in expected_level_pool)

    def test_generate_foe_character_level_three(self):
        character = {'Name': 'Oop', 'X-position': 0, 'Y-position': 0, 'Level': 3}
        expected_level_pool = [1, 2, 3]
        foe = generate_foe(character)
        self.assertTrue(foe['Required Level'] in expected_level_pool)

    def test_generate_foe_character_unchanged(self):
        character = {'Name': 'Oop', 'X-position': 0, 'Y-position': 0, 'Level': 3}
        generate_foe(character)
        self.assertEqual(character, {'Name': 'Oop', 'X-position': 0, 'Y-position': 0, 'Level': 3})
