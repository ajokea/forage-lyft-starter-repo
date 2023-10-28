from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage,current_mileage), SpindlerBattery(last_service_date))

    def create_thorex(last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage,current_mileage), NubbinBattery(last_service_date))

    def create_palindrome(last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date))

    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage,current_mileage), SpindlerBattery(last_service_date))

    def create_rorsacch(last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage,current_mileage), NubbinBattery(last_service_date))