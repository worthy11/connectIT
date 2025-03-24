class Structure:
    def __init__(self, name):
        self.name = name

    def render(self):
        print(self)

    def __str__(self) -> str:
        return "Base render() method"

class Unit(Structure):
    def __init__(self, name: str, color: str, pattern: str):
        super().__init__(name)
        self.color = color
        self.pattern = pattern
        self.color_codes = {
            'red': '\033[91m',
            'blue': '\033[94m',
            'green': '\033[92m',
            'white': '\033[97m',
            'black': '\033[90m'
        }

    def __str__(self) -> str:
        color_code = self.color_codes.get(self.color[1:-1], '')
        reset_code = '\033[0m'
        return f"{color_code}▲{reset_code}"

class Layer(Structure):
    def __init__(self, name: str, units: list[Unit]):
        super().__init__(name)
        self.units = units
        self.length = len(units)

    def add_unit(self, unit: Unit):
        self.units.append(unit)
        self.length += 1

    def remove_unit(self, index: int):
        self.units.pop(index)
        self.length -= 1

    def __str__(self):
        # Join the string representation of each unit (colored triangle) with a space
        units_str = " ".join(str(u) for u in self.units)
        return units_str

class Shape(Structure):
    def __init__(self):
        print("Shape declared")

class Model(Structure):
    def __init__(self):
        print("Model declared")