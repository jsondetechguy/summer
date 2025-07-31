class Car:
    def __init__(self, make, model, year, plate, color):
        self.make = make
        self.model = model
        self.year = year
        self.plate = plate
        self.color = color

    def drive(self):
        print("*vroom* you are driving")
    def stop(self):
        print("*beep* you stoped")