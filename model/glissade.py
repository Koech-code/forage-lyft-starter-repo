from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class glissade(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
