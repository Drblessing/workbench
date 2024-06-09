# Elevator Door class
class ElevatorDoor:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False


# Elevator Button class
class ElevatorButton:
    def __init__(self, floor):
        self.floor = floor
        # switch
        self.is_pressed = False

    def press(self):
        self.is_pressed = True


# Elevator Motor class
class ElevatorMotor:
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False


# Elevator class composed of Door, Buttons, and Motor
class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.door = ElevatorDoor()
        self.buttons = [ElevatorButton(floor) for floor in range(1, num_floors + 1)]
        self.motor = ElevatorMotor()

    def select_floor(self, floor):
        if 1 <= floor <= self.num_floors:
            self.buttons[floor - 1].press()

    def operate(self):
        if any(button.is_pressed for button in self.buttons):
            self.motor.start()
            self.door.open()
            self.door.close()
            self.motor.stop()
            print("Elevator arrived at a selected floor.")
        else:
            print("Elevator is idle.")


# Let's test the elevator composition
if __name__ == "__main__":
    num_floors = 5
    elevator = Elevator(num_floors)

    # Press some buttons to select floors
    elevator.select_floor(2)
    elevator.select_floor(4)
    elevator.select_floor(1)

    # Operate the elevator
    elevator.operate()
