"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count("Peanut is SOOO cute"), 9)

    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([[1, 2, 3], [1], [9, 9, 9, 9], []]), [])

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([[1, 2, 3], [1, 2], [9, 9, 9, 9], []]), [[1, 2]])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs([[2, 1], [4, 3], [6, 5]]), [[1, 2], [3, 4], [5, 6]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs([[], [1], [2, 1], [3, 4], [5, 6, 7]]), [[], [1], [1, 2], [3, 4], [5, 6, 7]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3, 5), data.Price(1, 1)), data.Price(4, 6))

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3, 90), data.Price(4, 20)), data.Price(8, 10))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(0, 2), data.Point(3, 0))), 6)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-4, -1), data.Point(-1, -6))), 15)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author("Peanut", [data.Book(["Peanut"], "Meow"), data.Book(["evil Peanut"], "Mew")]), [data.Book(["Peanut"], "Meow")])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author("Peanut", [data.Book(["Calabasa"], "Meow 2"), data.Book(["evil Peanut"], "Mew")]), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0, 4), data.Point(4, 0))), data.Circle(data.Point(2.0, 2.0), 2.0))

    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0, 4), data.Point(2, 0))), data.Circle(data.Point(1.0, 2.0), 2.0))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([data.Employee("Peanut", 110), data.Employee("Calabasa", 100), data.Employee("Queona", 90)]), [data.Employee("Queona", 90)])

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([]), [])


if __name__ == '__main__':
    unittest.main()