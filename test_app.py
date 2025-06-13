import unittest
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_random_fruit(self):
        fruit = app.random_fruit()
        self.assertIn(fruit, app.FRUITS, "Random should in list")
