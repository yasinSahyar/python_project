
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()
        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print("Elevator moved up to floor:", self.current_floor)
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print("Elevator moved down to floor:", self.current_floor)
        else:
            print("Elevator is already at the bottom floor.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm activated! All elevators are moving to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


# Main program
if __name__ == "__main__":
    # Create a new building with 3 elevators
    building = Building(1, 10, 3)

    # Run the elevators
    building.run_elevator(1, 5)  # Elevator 1 to floor 5
    building.run_elevator(2, 8)  # Elevator 2 to floor 8
    building.run_elevator(3, 2)  # Elevator 3 to floor 2

    # Activate fire alarm
    building.fire_alarm()












"""
Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the 
bottom floor. Continue the main program by causing a fire alarm in your building.


"""