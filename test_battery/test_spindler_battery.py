import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_to_be_serviced(self):
        current_date = date.fromisoformat("2022-05-06")
        last_service_date = date.fromisoformat("2019-06-21")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        current_date = date.fromisoformat("2022-05-06")
        last_service_date = date.fromisoformat("2022-01-04")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())