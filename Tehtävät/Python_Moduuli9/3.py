##
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def develop(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def print_information(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed}")
        print(f"Current Speed: {self.current_speed}")
        print(f"Travelled Distance: {self.travelled_distance}")

    def drive(self, hours):
        # Calculate distance travelled at constant speed
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

# Main program
if __name__ == "__main__":
    # Create a new car
    bmw = Car("ABC-123", 142)

    # Accelerate by +30 km/h
    bmw.develop(30)
    # Accelerate by +70 km/h
    bmw.develop(70)
    # Accelerate by +50 km/h
    bmw.develop(50)
    bmw.print_information()

    # Use emergency brake by forcing a -200 km/h change
    bmw.develop(-200)
    bmw.print_information()

    # Drive for 1.5 hours
    bmw.drive(1.5)

    # Print out the travelled distance
    print("Travelled Distance after driving for 1.5 hours:", bmw.travelled_distance, "km")




"""
Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method increases the travelled
 distance by how much the car has travelled in constant speed in the given time. Example: The travelled distance of car object is 2000 km. 
 The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
"""