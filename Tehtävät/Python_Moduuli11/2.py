class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed change is within bounds
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        # Calculate distance travelled at constant speed
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


# Main program
if __name__ == "__main__":
    # Create an electric car
    electric_car = ElectricCar("ABC-15", 180, 52.5)

    # Set speed for electric car
    electric_car.accelerate(120)

    # Drive electric car for three hours
    electric_car.drive(3)

    # Print out distance travelled by electric car
    print("Distance travelled by Electric Car:", electric_car.travelled_distance, "km")

    # Create a gasoline car
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Set speed for gasoline car
    gasoline_car.accelerate(150)

    # Drive gasoline car for three hours
    gasoline_car.drive(3)

    # Print out distance travelled by gasoline car
    print("Distance travelled by Gasoline Car:", gasoline_car.travelled_distance, "km")










    """
    Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the capacity of the battery 
    in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for 
    the subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity 
    as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main 
    program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds 
    for both cars, make them drive for three hours and print out the values of their kilometer counters.
    """
