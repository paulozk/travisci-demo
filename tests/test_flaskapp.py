import unittest

from main import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiply(self):
        # given
        x = 10
        y = 12
        # when
        answer = multiply(x, y)
        # then
        self.assertEqual(answer, 120)
    # TODO DEFINE TWO MORE TESTS ON THE END POINTS

    def test_hello(self):
        # given

        # when
        answer = hello()
        # then
        self.assertEqual("Hello World!", answer)

    def test_hello_sad(self):



    def test_to_uppercase(self):
        # given
        s = "hello"
        # when
        answer = to_uppercase(s)
        # then
        self.assertEqual("HELLO", answer)


if __name__ == '__main__':
    unittest.main()