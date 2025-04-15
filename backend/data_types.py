import numpy as np
import plotly.graph_objects as go

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

class Layer(Structure):
    def __init__(self, units: list[Unit], closed=False):
        super().__init__()
        self.units = list(units)
        self.closed = closed

        self.shift = 0
        self.level = 0
        self.radius = len(self.units) if self.closed else 0
        
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
        for x, unit in enumerate(self.units):
            if self.closed:
                arg = 360 / self.radius
                angle = (x + self.shift) * arg 
                unit.translate((0, self.radius / 6, self.level / 3 + self.radius / 6))
                unit.rotate((0, 0, angle-90))
            else:
                unit.translate(((self.shift + x) * 0.8, self.radius, self.level / 3))
            unit.render(fig)

        self.reset_state()

    def reset_state(self):
        self.x = self.y = self.z = 0
        self.rot_x = self.rot_y = self.rot_z = 0

class Shape(Structure):
    def __init__(self, layers: list[Layer], connections: list[dict]):
        super().__init__()
        self.layers = list(layers)
        self.connections = dict(connections)

    def update(self, layers: list, connections: dict):
        self.layers = list(layers)
        self.connections = dict(connections)

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
        shifts = [0]
        for idx in range(len(self.connections)):
            shifts.append(shifts[idx-1] + self.connections[idx]["shift"] + self.connections[idx]["type"]*0.5)

        for z, layer in enumerate(self.layers):
            layer.shift = shifts[z] # o ile unitów w prawo przekręcić layer
            layer.level = z
            layer.render(fig)
    
class Model(Structure):
    def __init__(self):
        print("Model declared")