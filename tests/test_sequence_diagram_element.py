import unittest

from models.diagrama_sequencia import SequenceDiagramElement
from parameterized import parameterized

class TestSequenceDiagramElement(unittest.TestCase):

    def setUp(self):
        self.sequence_diagram_element = SequenceDiagramElement()
        self.sequence_diagram_element2 = SequenceDiagramElement()

       
    def tearDown(self):
        self.sequence_diagram_element.dispose()
        self.sequence_diagram_element2.dispose()