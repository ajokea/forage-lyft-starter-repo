from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensor_readings):
        self.sensor_readings = sensor_readings

    def needs_service(self):
        if sum(self.sensor_readings) >= 3:
            return True
        else:
            return False