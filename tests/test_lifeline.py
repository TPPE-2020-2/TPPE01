import unittest
from models.lifeline import Lifeline
from parameterized import parameterized

class TestLifeline(unittest.TestCase):
    def setUp(self):
        self.lifeline = Lifeline()

    @parameterized.expand([
        ['1'],
        ['2'],
        ['3'],
    ])

    def test_set_id(self, id):
        self.lifeline.set_id(id)
        self.assertEqual(self.lifeline.get_id(), id)