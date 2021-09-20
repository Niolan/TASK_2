from unittest import TestCase, main
from anagrams.anagrams import palindrom as p

cases = [
    ('abed efgh', 'deba hgfe'),
    ('a1bcd efg!h', 'd1cba hgf!e'),
    ('', ''),
]

class Palindromtest(TestCase):
    def test_val(self):
        self.assertEqual(p('a1bcd efg!h'), 'd1cba hgf!e')
        for text, reversed_text in cases:
            with self.subTest():
                self.assertEqual(p(text), reversed_text)


if __name__ == '__main__':
    main()
