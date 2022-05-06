from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import nubbinBattery

class rorschach(WilloughbyEngine, nubbinBattery):
    def needs_service(self):
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
