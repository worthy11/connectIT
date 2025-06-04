import numpy as np
import plotly.graph_objects as go


def unit_to_multiunit(u):
    return MultiUnit(u, 1)

def unit_to_layer(u):
    return Layer([u], False)

def unit_to_shape(u):
    return Shape([Layer([u], False)], [])

def unit_to_model(u):
    return Model([Shape([Layer([u], False)], [])], [])

def multiunit_to_layer(mu):
    return Layer(mu.extract_units(), False)

def multiunit_to_shape(mu):
    return Shape([Layer(mu.extract_units(), False)], [])

def multiunit_to_model(mu):
    return Model([Shape([Layer(mu.extract_units(), False)], [])], [])

def layer_to_shape(l):
    return Shape([l], [])

def layer_to_model(l):
    return Model(Shape([l], []), [])

def shape_to_model(s):
    return Model([s], [])

def unit_to_number(u):
    return 1

def unit_to_boolean(u):
    return True

def multiunit_to_number(mu):
    return mu.number

def layer_to_number(l):
    return len(l)

def shape_to_number(s):
    return len(s.layers)

def model_to_number(m):
    return len(m.shapes)

def any_to_boolean(x):
    return True

def number_to_boolean(x):
    return x > 0

type_map = {
    "UNIT": {
        "MULTI_UNIT": unit_to_multiunit,
        "LAYER": unit_to_layer,
        "SHAPE": unit_to_shape,
        "MODEL": unit_to_model
        },
    "MULTI_UNIT": {"LAYER": multiunit_to_layer, "SHAPE": multiunit_to_shape, "MODEL": multiunit_to_model},
    "LAYER": {"SHAPE": layer_to_shape, "MODEL": layer_to_model},
    "SHAPE": {"MODEL": shape_to_model},
    "MODEL": {},
    "NUMBER": {},
    "BOOLEAN": {},
    "FUNCTION": {}
}

cast_map = {
    "UNIT": {"NUMBER": unit_to_number, "BOOLEAN": any_to_boolean},
    "MULTI_UNIT": {"NUMBER": multiunit_to_number, "BOOLEAN": any_to_boolean},
    "LAYER": {"NUMBER": layer_to_number, "BOOLEAN": any_to_boolean},
    "SHAPE": {"NUMBER": shape_to_number, "BOOLEAN": any_to_boolean},
    "MODEL": {"NUMBER": model_to_number, "BOOLEAN": any_to_boolean},
    "NUMBER": {"BOOLEAN": number_to_boolean},
    "BOOLEAN": {"NUMBER": lambda x: 1 if x else 0},
}

class Structure:
    def render(self):
        print(self)

    def __str__(self) -> str:
        return "Base render() method"

class Unit(Structure):
    def __init__(self, color: str="WHITE", pattern: str="NONE"):
        super().__init__()
        self.color = color
        self.pattern = pattern
        self.color_map = {
            "red": "rgb(255, 0, 0)",
            "green": "rgb(0, 255, 0)",
            "blue": "rgb(0, 0, 255)",
            "white": "rgb(255, 255, 255)",
            "black": "rgb(0, 0, 0)",
            "yellow": "rgb(255, 255, 0)",
            "lilac": "rgb(246, 159, 255)"
        }
        self.x = self.y = self.z = 0

        self.vertices = np.array([
            [0, -0.5, -0.5],
            [+0.2, 0, -0.5],
            [0, 0.5, -0.5],
            [-0.2, 0, -0.5],
            [+0.1, -0.5, 0.5],
            [-0.1, -0.5, 0.5],
        ])

        faces = [
            (0, 1, 2, 3),
            (0, 1, 4), (1, 2, 4),
            (0, 3, 5), (3, 2, 5),
            (0, 2, 4), (0, 2, 5)
        ]
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0), (0, 2),
            (0, 4), (4, 2),
            (0, 5), (5, 2)
        ]
        self.i_faces = []
        self.j_faces = []
        self.k_faces = []

        for face in faces:
            if len(face) == 3:
                self.i_faces.append(face[0])
                self.j_faces.append(face[1])
                self.k_faces.append(face[2])
            else:
                self.i_faces.append(face[0])
                self.j_faces.append(face[1])
                self.k_faces.append(face[2])
                
                self.i_faces.append(face[0])
                self.j_faces.append(face[2])
                self.k_faces.append(face[3])

    def __str__(self) -> str:
        if str(self.pattern) == "None":
            return f"*{self.color}*"
        print(self.pattern)
        return f"*{self.color}* *{self.pattern}*"

    def __copy__(self):
        return Unit(self.color, self.pattern)

    def translate(self, vector=(0, 0, 0)):
        self.vertices[:, 0] += vector[0]
        self.vertices[:, 1] += vector[1]
        self.vertices[:, 2] += vector[2]

    def rotate(self, angle = (0, 0, 0)):
        x, y, z = np.radians(angle[0]), np.radians(angle[1]), np.radians(angle[2])
        cos_x, sin_x = np.cos(x), np.sin(x)
        cos_y, sin_y = np.cos(y), np.sin(y)
        cos_z, sin_z = np.cos(z), np.sin(z)

        Rx = np.array([
            [1, 0, 0],
            [0, cos_x, -sin_x],
            [0, sin_x, cos_x]
        ])
        Ry = np.array([
            [cos_y, 0, sin_y],
            [0, 1, 0],
            [-sin_y, 0, cos_y]
        ])
        Rz = np.array([
            [cos_z, -sin_z, 0],
            [sin_z, cos_z, 0],
            [0, 0, 1]
        ])

        R = Rz @ Ry @ Rx

        self.vertices = np.dot(self.vertices, R.T)

    def reset_state(self):
        self.x = self.y = self.z = 0
        self.vertices = np.array([
            (-0.25, -0.5, -0.5),
            (+0.25, -0.5, -0.5),
            (+0.25, 0.5, -0.5),
            (-0.25, 0.5, -0.5),
            (-0.15, -0.5, 0.5),
            (+0.15, -0.5, 0.5)
        ])

    def render(self, fig):
        x_vals, y_vals, z_vals = zip(*(self.vertices))
        fig.add_trace(go.Mesh3d(
            x=x_vals, y=y_vals, z=z_vals,
            i=self.i_faces, j=self.j_faces, k=self.k_faces,
            color=self.color_map[self.color.lower()],
            opacity=1,
            lighting=dict(specular=0.1, diffuse=1.0, ambient=0.8, fresnel=0)
        ))

        color = "BLACK"
        if self.color == "BLACK":
            color = "gray"
        for edge in self.edges:
            fig.add_trace(go.Scatter3d(
                x=[x_vals[edge[0]], x_vals[edge[1]]],
                y=[y_vals[edge[0]], y_vals[edge[1]]],
                z=[z_vals[edge[0]], z_vals[edge[1]]],
                mode="lines",
                line=dict(color=color, width=4)
            ))
        self.reset_state()

class MultiUnit():
    def __init__(self, u: Unit=Unit(), n: int=1):
        self.unit = u.__copy__()
        self.number = n

    def extract_units(self):
        return [self.unit] * self.number

class Layer(Structure):
    def __init__(self, units: list[Unit]=[], closed=False):
        super().__init__()
        self._units = []
        self._closed = closed
        self._radius = 0 if self._closed else -1
        for u in units:
            self.add_unit(u)
        self.x = self.y = self.z = 0
        self.rot_x = self.rot_y = self.rot_z = 0

    def __copy__(self):
        return Layer(self._units, self._closed)
    
    def __len__(self):
        return len(self._units)

    def __str__(self):
        if self._closed:
            return f"{self._units}, CLOSED"
        return f"[{', '.join([str(unit) for unit in self._units])}]"

    def add_unit(self, u: Unit):
        self._units.append(u.__copy__())
        if self._closed:
            self._radius += 1

    def add_multi_unit(self, mu: MultiUnit):
        units = mu.extract_units()
        for u in units:
            self.add_unit(u)
            
    def add_layer(self, l):
        units = l._units
        for u in units:
            self.add_unit(u)

    def remove_unit(self, index: int):
        self._units.pop(index)
        if self._closed:
            self._radius -= 1

    def translate(self, vector = (0, 0, 0)):
        self.x += vector[0]
        self.y += vector[1]
        self.z += vector[2]

    def rotate(self, angle = (0, 0, 0)):
        self.rot_x += angle[0]
        self.rot_y += angle[1]
        self.rot_z += angle[2]

    def set_closed(self, closed):
        if closed:
            self.set_length(len(self))
        self._closed = closed

    def set_length(self, length):
        self._radius = length

    def is_closed(self):
        return self._closed

    def render(self, fig, shift=0, z=0):
        for idx, unit in enumerate(self._units):
            x = y = arg = 0
            if self._closed:
                angle = 360 / self._radius
                arg = (idx + shift*0.5) * angle
                x = self._radius / 10 * -np.sin(np.deg2rad(arg))
                y = self._radius / 10 * np.cos(np.deg2rad(arg))
            else:
                x = (idx + shift*0.5) / 2
                arg = 0
            unit.rotate((0, 0, arg))
            unit.translate((x, y, z/2))
            unit.render(fig)
        self.reset_state()

    def reset_state(self):
        self.x = self.y = self.z = 0
        self.rot_x = self.rot_y = self.rot_z = 0

class Shape(Structure):
    def __init__(self, layers: list[Layer]=[], connections: list[dict]=[]):
        super().__init__()
        self.layers = []
        self.connections = []
        self.base_length = -1
        for l, c in zip(layers, [{"type": 0, "shift": 0}] + connections):
            self.add_layer(l, c)

    def __copy__(self):
        return Shape(self.layers, self.connections)

    def __str__(self):
        return f"[{', '.join([str(layer) for layer in self.layers])}]"

    def add_layer(self, l: Layer, c: dict):
        self.layers.append(l.__copy__())
        self.connections.append(c)

    def add_shape(self, s, c: dict):
        layers = s.layers
        connections = [c] + s.connections
        for l, c in zip(layers, connections):
            self.add_layer(l, c)

    def remove_layer(self):
        if self.layers:
            self.layers.pop()  
            self.connections.pop()

    def bend(self, start, end, angle):
        x = self.radius * np.cos(np.deg2rad(angle))
    
    def render(self, fig, stack=0, shift=0):
        shifts = [shift + self.connections[0]["shift"]*2 + self.connections[0]["type"]]
        for idx, c in enumerate(self.connections[1:]):
            shifts.append(shifts[idx] + c["shift"]*2 + c["type"])

        for z, layer in enumerate(self.layers):
            layer.render(fig, shift=shifts[z], z=z+stack)
    
class Model(Structure):
    def __init__(self, shapes: list[Shape]=[], connections: list[dict]=[]):
        self.shapes = []
        self.connections = []
        for s, c in zip(shapes, [{"from": 0, "to": 0, "type": 0, "shift": 0}] + connections):
            self.add_shape(s, c)
        self.closed = False
        self.top = []
        self.base_length = 0

    def add_shape(self, s: Shape, c: dict):
        if c.get("from") is not None:
            self.base_length = len(s.layers[0])
            self.top = [0 for _ in range(self.base_length*2)]
            self.shapes.append(s.__copy__())
            self.connections.append(c)
            return
            
        if s.layers[0]._closed and len(s.layers[0]) != self.base_length:
            raise Exception("Boom1")
        for l in s.layers:
            if len(l) > self.base_length:
                raise Exception("Boom2")
        
        type = c["type"]
        shift = c["shift"]
        _from = self.top[shift+type]
        to = len(self.shapes)
        for index in range(len(s.layers[0])):
            if self.top[index] != _from:
                raise Exception("Boom3")
            self.top[index] = to
            
        c["from"] = _from
        c["to"] = to
        self.shapes.append(s.__copy__())
        self.connections.append(c)

    def add_model(self, m, c: dict):
        shapes = m.shapes
        connections = [c] + m.connections
        for s, c in zip(shapes, connections):
            self.add_shape(s, c)

    def render(self, fig):
        stack = 0
        shifts = [self.connections[0]["shift"]*2 + self.connections[0]["type"]]
        for idx, s in enumerate(self.shapes):
            s.render(fig, stack=stack, shift=shifts[idx])
            stack += len(s.layers)