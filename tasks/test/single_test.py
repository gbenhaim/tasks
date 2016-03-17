from ..single import *
import unittest


class SingletonTest(unittest.TestCase):
    """Tests for the singleton task"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method_1(self):
        """
        test for method1
        :return:
        """
        f = Foo.get_instance()
        g = Foo.get_instance()
        self.assertTrue(f is g)

    def test_method_2(self):
        """
        test for method2
        :return:
        """
        @make_it_singleton
        class Goo:
            def __init__(self, name):
                self.name = name

        a = Goo("gal")
        b = Goo("tomer")
        self.assertTrue(a is b)

    def test_method_3(self):
        """
        test for method3
        :return:
        """
        @MakeItSingleton
        class Goo:
            def __init__(self, name):
                self.name = name

        a = Goo("gal")
        b = Goo("tomer")
        self.assertTrue(a is b)


if __name__ == '__main__':
    unittest.main()
