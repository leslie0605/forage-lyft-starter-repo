from car import Car
from engine import Engine
from battery import Battery

class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = Engine(current_mileage, last_service_mileage)
        self.battery = Battery(last_service_date, current_date)
        return self
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = Engine(current_mileage, last_service_mileage)
        self.battery = Battery(last_service_date, current_date)
        return self
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = Engine(current_mileage, last_service_mileage)
        self.battery = Battery(last_service_date, current_date)
        return self
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = Engine(current_mileage, last_service_mileage)
        self.battery = Battery(last_service_date, current_date)
        return self
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = Engine(current_mileage, last_service_mileage)
        self.battery = Battery(last_service_date, current_date)
        return self