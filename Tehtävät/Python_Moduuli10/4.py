
import random

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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print("Race:", self.name)
        print("{:<15} {:<15} {:<20}".format("Registration", "Current Speed", "Travelled Distance (km)"))
        for car in self.cars:
            print("{:<15} {:<15} {:<20}".format(car.registration_number, car.current_speed, car.travelled_distance))
        print()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# Main program
if __name__ == "__main__":
    # Create a list of 10 cars for the race
    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    # Create a race
    grand_demo_derby = Race("Grand Demolition Derby", 8000, cars)

    # Simulate race progress
    hour = 0
    while not grand_demo_derby.race_finished():
        grand_demo_derby.hour_passes()
        hour += 1
        if hour % 10 == 0:
            print("Race progress after", hour, "hours:")
            grand_demo_derby.print_status()

    # Print final status
    print("Final race status:")
    grand_demo_derby.print_status()















"""
This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties:
 name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers,
  and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:

    ¤ hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car
      and calls their drive method.
    ¤ print_status, which prints out the current information of each car as a clear, formatted table.
    ¤ race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly
to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses
the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours
and then once more at the end of the race.

"""