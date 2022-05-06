import unittest

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_engine_needs_service(self):
        current_mileage = 300010
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_needs_no_service(self):
        current_mileage = 28002
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())