import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tires_array = [0,1,0,2]
        tires = OctoprimeTire(tires_array)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        tires_array = [0,1,0,1]
        tires = OctoprimeTire(tires_array)
        self.assertFalse(tires.needs_service())