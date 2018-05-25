import unittest

from terminaltables import AsciiTable

import app


class TestAppMainMethod(unittest.TestCase):
    def test_main(self):
        actual = app.main()
        expected = AsciiTable([['Message'], ['It works fine!']], title='Info').table
        self.assertEquals(actual, expected, 'Expected:\n{0}\n\nActual:\n{1}'.format(expected, actual))


if __name__ == '__main__':
    unittest.main()
