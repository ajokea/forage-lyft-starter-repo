from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    def create_calliope(last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(last_service_mileage,current_mileage), SpindlerBattery(last_service_date), CarriganTires(tire_wear))

    def create_thorex(last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(last_service_mileage,current_mileage), NubbinBattery(last_service_date), OctoprimeTires(tire_wear))

    def create_palindrome(last_service_date, warning_light_on, tire_wear):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date), CarriganTires(tire_wear))

    def create_glissade(last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(last_service_mileage,current_mileage), SpindlerBattery(last_service_date), OctoprimeTires(tire_wear))

    def create_rorsacch(last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(last_service_mileage,current_mileage), NubbinBattery(last_service_date), CarriganTires(tire_wear))