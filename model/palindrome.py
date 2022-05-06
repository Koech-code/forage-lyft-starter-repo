from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Calliope(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
