import unittest
from models.message import Message
from parameterized import parameterized

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message()

    @parameterized.expand([
        ['Origem 1'],
        ['Origem 2'],
        ['Origem 3'],
    ])
    def test_set_source(self, source):
        self.message.set_source(source)
        self.assertEqual(self.message.get_source(), source)

    @parameterized.expand([
        ['Destino 1'],
        ['Destino 2'],
        ['Destino 3'],
    ])
    def test_set_target(self, target):
        self.message.set_target(target)
        self.assertEqual(self.message.get_target(), target)

    @parameterized.expand([
        [1.0],
        [0.0],
        [0.5],
    ])
    def test_set_prob(self, prob):
        self.message.set_prob(prob)
        self.assertEqual(self.message.get_prob(), prob)
    
    @parameterized.expand([
        ['Sync'],
        ['Async'],
        ['Reply'],
    ])
    def test_set_message_type(self, message_type):
        self.message.set_message_type(message_type)
        self.assertEqual(self.message.get_message_type(), message_type)
