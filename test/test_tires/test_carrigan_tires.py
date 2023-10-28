import unittest

import sys
sys.path.append("/Users/ekoja/Documents/Coding/Forage/forage-lyft-starter-repo")

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        readings = [0,0,0,0.9]
        tires = CarriganTires(readings)
        self.assertTrue(tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        readings = [0,0,0,0.8]
        tires = CarriganTires(readings)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
    