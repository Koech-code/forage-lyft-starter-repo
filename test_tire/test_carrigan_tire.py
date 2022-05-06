import unittest

from tire.carrigan_tire import carriganTire


class testCarriganTire(unittest.TestCase):
    def test_tire_needs_to_be_serviced(self):
        newTestWearArray=0
        serviceCarrigan=carriganTire(newTestWearArray)
        self.assertTrue(serviceCarrigan.needs_service())

    def test_tire_does_not_need_service(self):
        newTestWearArray=4
        serviceCarrigan=carriganTire(newTestWearArray)
        self.assertFalse(serviceCarrigan.needs_service())