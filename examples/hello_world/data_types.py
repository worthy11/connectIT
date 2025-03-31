import numpy as np
import plotly.graph_objects as go

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
        self.color_map = {
            "red": "rgb(255, 0, 0)",
            "green": "rgb(0, 255, 0)",
            "blue": "rgb(0, 0, 255)",
            "white": "rgb(255, 255, 255)",
            "black": "rgb(0, 0, 0)"
        }

        self.x = self.y = self.z = 0
        self.vertices = np.array([
            [-0.25, -0.5, -0.5],
            [+0.25, -0.5, -0.5],
            [+0.25, 0.5, -0.5],
            [-0.25, 0.5, -0.5],
            [-0.25, -0.5, 0.5],
            [+0.25, -0.5, 0.5]
        ])

        faces = [
            (0, 3, 4), (1, 2, 5),  # Bottom and top triangles
            (0, 1, 2, 3), (0, 1, 5, 4), (4, 5, 2, 3)  # Side rectangles
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

        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0), # Bottom triangle
            (1, 5), (5, 4), (4, 0),  # Top triangle
            (4, 3), (5, 2)   # Vertical edges
        ]

    def __str__(self) -> str:
        color_code = self.color_codes.get(self.color, '')
        reset_code = '\033[0m'
        return f"{color_code}▲{reset_code}"
    
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
        # print("Render Unit")
        x_vals, y_vals, z_vals = zip(*(self.vertices))
        fig.add_trace(go.Mesh3d(
            x=x_vals, y=y_vals, z=z_vals,
            i=self.i_faces, j=self.j_faces, k=self.k_faces,
            color=self.color_map[self.color],
            opacity=1,
            lighting=dict(ambient=0.7, diffuse=0.6, specular=0.2, roughness=0.1)
        ))

        for edge in self.edges:
            fig.add_trace(go.Scatter3d(
                x=[x_vals[edge[0]], x_vals[edge[1]]],
                y=[y_vals[edge[0]], y_vals[edge[1]]],
                z=[z_vals[edge[0]], z_vals[edge[1]]],
                mode="lines",
                line=dict(color="black", width=4)
            ))
        self.reset_state()

class Layer(Structure):
    def __init__(self, name: str, units: list[Unit], closed=False):
        super().__init__(name)
        self.units = units
        self.closed = closed
        if closed:
            self.radius = len(self.units)
        else:
            self.radius = 0
        self.x = self.y = self.z = 0
        self.rot_x = self.rot_y = self.rot_z = 0

    def add_unit(self, unit: Unit):
        self.units.append(unit)

    def remove_unit(self, index: int):
        self.units.pop(index)

    def translate(self, vector = (0, 0, 0)):
        self.x += vector[0]
        self.y += vector[1]
        self.z += vector[2]

    def rotate(self, angle = (0, 0, 0)):
        self.rot_x += angle[0]
        self.rot_y += angle[1]
        self.rot_z += angle[2]

    def render(self, fig):
        # print("Render Layer")
        if self.closed:
            mod = 0.15 * (2*self.z + len(self.units)) # numer warstwy * długość
            arg = 360 / len(self.units)

            for x, unit in enumerate(self.units):
                angle = (x + self.rot_z) * arg 
                unit.rotate((-90, 0, angle-90))
                unit.translate((mod*(np.cos(np.radians(angle))), mod*(np.sin(np.radians(angle))), 0))
                unit.render(fig)
        else:
            for x, unit in enumerate(self.units):
                unit.translate((x+0.15, 0, self.z))
                unit.render(fig)
        self.reset_state()

    def reset_state(self):
        self.x = self.y = self.z = 0
        self.rot_x = self.rot_y = self.rot_z = 0

class Shape(Structure):
    def __init__(self, name: str, layers: list[Layer], connections: list[dict]):
        super().__init__(name)
        self.layers = layers
        self.connections = [{"type": 0, "shift": 0}] + connections

    def add_layer(self, layer : Layer, connection_type: str = "between", offset: int = 0):
        self.layers.append(layer)
        self.connections.append({"type": connection_type, "offset": offset})
    
    def remove_layer(self):
        if self.layers:
            self.layers.pop()  
            self.connections.pop()

    def __str__(self):
        return "\n".join(str(layer) for layer in self.layers)
    
    def render(self, fig):
        # print("Render Shape")

        for z, (layer, connection) in enumerate(zip(self.layers, self.connections)):
            # layer.closed = True
            if layer.closed:
                # layer.rotate((-90, 0, 0))
                layer.translate((0, 0, z))
                layer.rotate((0, 0, connection["shift"] + connection["type"] * 0.5))
            else:
                layer.translate((connection["shift"] + connection["type"] * 0.5, 0, z))
            layer.render(fig)
    
class Model(Structure):
    def __init__(self):
        print("Model declared")