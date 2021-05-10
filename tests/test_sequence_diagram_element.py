import unittest

from models.sequence_diagram_element import SequenceDiagramElement
from parameterized import parameterized

class TestSequenceDiagramElement(unittest.TestCase):

    def setUp(self):
        self.sequence_diagram_element = SequenceDiagramElement()
        self.sequence_diagram_element2 = SequenceDiagramElement()

    @parameterized.expand([
        ['Elemento 1'],
        ['Elemento 2'],
        ['Elemento 3'],
    ])
    def test_set_name(self, name):
        self.sequence_diagram_element.set_name(name)
        self.assertEqual(self.sequence_diagram_element.get_name(), name)
       
    def tearDown(self):
        self.sequence_diagram_element.dispose()
        self.sequence_diagram_element2.dispose()