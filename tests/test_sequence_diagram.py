import unittest

from models.diagrama_sequencia import SequenceDiagram
from models.diagrama_sequencia import SequenceDiagramElement
from parameterized import parameterized


class TestSequenceDiagram(unittest.TestCase):

    def setUp(self):
        self.sequence_diagram = SequenceDiagram()
    
    @parameterized.expand([
        ['Condition 1'],
        ['Condition 2'],
        ['Condition 3'],
    ])

    def tearDown(self):
        self.sequence_diagram.dispose()