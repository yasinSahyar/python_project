class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def devolop(self,change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0 :
            self.current_speed = 0
# Create a new car
bmw = Car("ABC-123", 142)

    # Print out all properties of the new car
print("Registration Number:", bmw.registration_number)
print("Maximum Speed:", bmw.max_speed, "km/h")
print("Current Speed:", bmw.current_speed, "km/h")
print("Travelled Distance:", bmw.travelled_distance, "km")