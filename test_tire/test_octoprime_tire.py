import unittest

from tire.octoprime_tire import octoprimeTire


class testOctoprimeTire(unittest.TestCase):
    def test_tire_needs_to_be_serviced(self):
        newTestWearArray=4
        serviceCarrigan=octoprimeTire(newTestWearArray)
        self.assertTrue(serviceCarrigan.needs_service())

    def test_tire_does_not_need_service(self):
        newTestWearArray=2
        serviceCarrigan=octoprimeTire(newTestWearArray)
        self.assertFalse(serviceCarrigan.needs_service())