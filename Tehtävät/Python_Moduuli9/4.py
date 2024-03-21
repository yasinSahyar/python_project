#
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

# Main program
if __name__ == "__main__":
    # Create a list of 10 cars
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        registration_number = f"ABC-{i}"
        cars.append(Car(registration_number, max_speed))

    # Start the race
    race_finished = False
    hour = 0
    while not race_finished:
        print(f"Hour {hour}:")
        # Update each car's speed
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

        # Drive each car for one hour
        for car in cars:
            car.drive(1)

        # Check if any car has travelled at least 10,000 km
        for car in cars:
            if car.travelled_distance >= 10000:
                race_finished = True
                break

        hour += 1

    # Print out properties of each car in a table format
    print("\nRace Results:")
    print("{:<15} {:<15} {:<15} {:<20}".format("Registration", "Max Speed (km/h)", "Current Speed", "Travelled Distance (km)"))
    for car in cars:
        print("{:<15} {:<15} {:<15} {:<20}".format(car.registration_number, car.max_speed, car.current_speed, car.travelled_distance))







"""

Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list
 that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
 The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following
  operations are performed:

    ¤ The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the
    accerelate method.
    ¤ Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.
"""