import unittest
from tire.carrigan_tire import CarriganTire

class TestCarrianTire(unittest.TestCase):
    def test_needs_service_true(self):
        tires_array = [0,0,0,0.9]
        tires = CarriganTire(tires_array)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        tires_array = [0,0,0,0.8]
        tires = CarriganTire(tires_array)
        self.assertFalse(tires.needs_service())