#student name: Michael Lin
#student ID: 101484021

class Vehicle:
    _valid_colors = {"red", "orange", "green", "yellow", "blue"}
    _valid_doors = {2, 4, 5}

    def __init__(self, color, doors, gas_powered):
        self.__color = color
        self.__doors = doors
        self.__gas_powered = gas_powered

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and value.lower() in self.__valid_colors:
            self.__color = value.lower()
        else:
            raise ValueError(f"Invalid color. Choose from: {', '.join(self.__valid_colors)}")

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, value):
        if value in self.__valid_doors:
            self.__doors = value
        else:
            raise ValueError(f"Invalid amount of doors, choose from: {self.__valid_doors}")

    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        if isinstance(value, bool):
            self.__gas_powered = value
        else:
            raise ValueError("Invalid value for gas powered, it needs to be a boolean.")

    def is_eco_friendly(self):
        return self.__doors == 2 and not self.__gas_powered

    def __str__(self):
        return (f"Vechile(color: {self.__color}, doors: {self.__doors}, gas powered: {self.__gas_powered}, "
                f"seats: {self.__seats})")

class Truck(Vehicle):
    def __init__(self, color, doors, gas_powered, seats, trunk_space):
        super().__init__(color, doors, gas_powered)
        self.__seats = seats
        self.__trunk_space = trunk_space

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if isinstance(value, int) and value > 0:
            self.__seats = value
        else:
            raise ValueError("Invalid number of seats. Needs to be greater then zero.")

    @property
    def trunk_space(self):
        return self.__trunk_space

    @trunk_space.setter
    def trunk_space(self, value):
        if isinstance(value, int) and value > 0:
            self.__trunk_space = value
        else:
            raise ValueError("Invalid trunk space. Must be greater then zero.")

    def is_eco_friendly(self):
        return super().is_eco_friendly() and self.__seats <= 2 and self.__trunk_space == 0

    def str(self):
        return (f"Truck(color: {self.__color}, doors: {self.__doors}, gas powered: {self.__gas_powered}, "
                f"seats: {self.__seats}, trunk space: {self.__trunk_space})")