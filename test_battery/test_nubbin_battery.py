import unittest
from datetime import date

from battery.nubbin_battery import nubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_to_be_serviced(self):
        current_date = date.fromisoformat("2022-05-06")
        last_service_date = date.fromisoformat("2017-08-12")
        battery = nubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        current_date = date.fromisoformat("2022-05-06")
        last_service_date = date.fromisoformat("2020-10-01")
        battery = nubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())