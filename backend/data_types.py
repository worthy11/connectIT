import numpy as np
import plotly.graph_objects as go

types = {
    0: "UNIT", # *red* *striped*
    1: "MULTI_UNIT", # 2 * (*red* *striped*), u * 2, [u]
    2: "LAYER", # 2*u <-> b*5 <-> g, [2*u]
    3: "SHAPE", # l1 <- ([g] <-> [b]) <<- [2*u] <-(5)- l4
    4: "MODEL",
    5: "NUMBER",
    6: "BOOLEAN"
}

class Structure:
    def render(self):
        print(self)

    def __str__(self) -> str:
        return "Base render() method"

class Unit(Structure):
    def __init__(self, color: str, pattern: str):
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
            [+0.2, -0.5, 0.5],
            [-0.2, -0.5, 0.5],
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
            (-0.25, -0.5, 0.5),
            (+0.25, -0.5, 0.5)
        ])

    def render(self, fig):
        x_vals, y_vals, z_vals = zip(*(self.vertices))
        fig.add_trace(go.Mesh3d(
            x=x_vals, y=y_vals, z=z_vals,
            i=self.i_faces, j=self.j_faces, k=self.k_faces,
            color=self.color_map[self.color],
            opacity=1,
            lighting=dict(specular=0.1, diffuse=1.0, ambient=0.5, fresnel=0)
        ))

        color = "black"
        if self.color == "black":
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
    def __init__(self, u: Unit, n: int=1):
        self.unit = u.__copy__()
        self.number = n

    def extract_units(self):
        return [self.unit] * self.number

class Layer(Structure):
    def __init__(self, units: list[Unit], closed=False):
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

    def add_unit(self, u: Unit):
        self._units.append(u.__copy__())
        if self._closed:
            self._radius += 1

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
                x = self._radius / 5 * -np.sin(np.deg2rad(arg))
                y = self._radius / 5 * np.cos(np.deg2rad(arg))
            else:
                x = idx
                arg = 0
            unit.rotate((0, 0, arg))
            unit.translate((x, y, z/2))
            unit.render(fig)
        self.reset_state()

    def reset_state(self):
        self.x = self.y = self.z = 0
        self.rot_x = self.rot_y = self.rot_z = 0

class Shape(Structure):
    def __init__(self, layers: list[Layer], connections: list[dict]=[]):
        super().__init__()
        self.layers = []
        self.connections = []
        self.base_length = -1
        for l, c in zip(layers, [{"type": 0, "shift": 0}] + connections):
            self.add_layer(l, c)

    def __copy__(self):
        return Shape(self.layers, self.connections)

    def add_layer(self, l: Layer, c: dict):
        self.layers.append(l.__copy__())
        self.connections.append(c)

    def remove_layer(self):
        if self.layers:
            self.layers.pop()  
            self.connections.pop()

    def bend(self, start, end, angle):
        x = self.radius * np.cos(np.deg2rad(angle))
    
    def render(self, fig, stack=0):
        shifts = [self.connections[0]["shift"]*2 + self.connections[0]["type"]]
        for idx, c in enumerate(self.connections[1:]):
            shifts.append(shifts[idx] + c["shift"]*2 + c["type"])

        for z, layer in enumerate(self.layers):
            layer.render(fig, shift=shifts[z], z=z+stack)
    
class Model(Structure):
    def __init__(self, shapes: list[Shape], connections: list[dict]=[]):
        self.shapes = [s.__copy__() for s in shapes]
        self.connections = [c for c in connections]
        self.free = []

    def update_free(self):
        base_length = len(self.shapes[0].layers[0])
        for s in self.shapes:
            for l in s.layers:
                self.free.append([False for _ in range(base_length*2)])

        for l_i, l in enumerate([l for s in self.shapes for l in s.layers][1:]):
            shift = l.shift
            length = len(l.units)
            for _ in range(shift, shift+length):
                self.free[l_i-1][_] = False
