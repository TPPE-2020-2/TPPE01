import unittest
from models.fragment import Fragment
from parameterized import parameterized


class TestActivityDiagram(unittest.TestCase):

    def setUp(self):
        self.fragment = Fragment()
    
    @parameterized.expand([
        ['Diagrama 1'],
        ['Diagrama 2'],
        ['Diagrama 3'],
    ])
    def test_set_represented_by(self, represented_by):
        self.fragment.set_represented_by(represented_by)
        self.assertEqual(self.fragment.get_represented_by(), represented_by)
    
    
