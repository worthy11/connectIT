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
        self.x = self.y = self.z = 0

    def __str__(self) -> str:
        color_code = self.color_codes.get(self.color[1:-1], '')
        reset_code = '\033[0m'
        return f"{color_code}▲{reset_code}"
    
    def set_position(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z

class Layer(Structure):
    def __init__(self, name: str, units: list[Unit]):
        super().__init__(name)
        self.units = units

    def add_unit(self, unit: Unit):
        self.units.append(unit)

    def remove_unit(self, index: int):
        self.units.pop(index)

    def __str__(self):
        # Join the string representation of each unit (colored triangle) with a space
        units_str = " ".join(str(u) for u in self.units)
        return units_str

class Shape(Structure):
    def __init__(self, name: str, layers: list[Layer]):
        super().__init__(name)
        self.layers = layers
        self.connections = []

    def add_layer(self, layer : Layer, connection_type: str = "between", offset: int = 0):
        self.layers.append(layer)
        self.connections.append({"type": connection_type, "offset": offset})
    
    def remove_layer(self):
        if self.layers:
            self.layers.pop()  
            self.connections.pop()

    def __str__(self):
        return "\n".join(str(layer) for layer in self.layers)
    
class Model(Structure):
    def __init__(self):
        print("Model declared")