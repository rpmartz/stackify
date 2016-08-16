import unittest

from app import remove_non_letters


class TestConvertingStackNames(unittest.TestCase):
    def test_letters_are_uppercased(self):
        self.assertEqual('ABC', remove_non_letters('abc'))

    def test_numbers_are_removed(self):
        self.assertEqual('ABC', remove_non_letters('a1B2c3'))

    def test_spaces_are_removed(self):
        self.assertEqual('MEAN', remove_non_letters('m E a N !!'))


if __name__ == '__main__':
    unittest.main()
