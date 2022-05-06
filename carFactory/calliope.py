from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
