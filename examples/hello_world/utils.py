from data_types import *
import plotly.graph_objects as go

color_map = {
    "red": "rgb(255, 0, 0)",
    "green": "rgb(0, 255, 0)",
    "blue": "rgb(0, 0, 255)",
    "white": "rgb(255, 255, 255)",
    "black": "rgb(0, 0, 0)"
}

def render_model(fig, model: Model | list):
    for z, shape in enumerate(model):
        render_layer(fig, shape, z)

def render_shape(fig, shape: Shape, z: int):
    for y, layer in enumerate(shape):
        render_layer(fig, layer, y, z)

def render_layer(fig, layer: Layer, y: int, z: int):
    for x, unit in enumerate(layer.units):
        render_unit(fig, unit, x, y, z)

def render_unit(fig, unit: Unit, x: int, y: int, z: int):
    vertices = [
        [x, y, z],        # Bottom-left corner
        [x + 1, y, z],    # Bottom-right corner
        [x + 0.5, y + 1, z],  # Top corner
        [x + 0.5, y + 0.5, z + 0.5]  # Center raised point
    ]

    i, j, k = 0, 1, 2  # Front triangle
    a, b, c = 0, 2, 3  # Left side
    d, e, f = 1, 2, 3  # Right side
    g, h, i = 0, 1, 3  # Bottom side

    fig.add_trace(go.Mesh3d(
        x=[v[0] for v in vertices],
        y=[v[1] for v in vertices],
        z=[v[2] for v in vertices],
        color=color_map[unit.color[1:-1]],
        opacity=0.9,
        i=[i, a, d, g],
        j=[j, b, e, h],
        k=[k, c, f, i]
    ))

def show_figure(fig, structure: Structure):
    if isinstance(structure, Unit):
        render_unit(fig, structure, 0, 0, 0)
    elif isinstance(structure, Layer):
        render_layer(fig, structure, 0, 0)
    elif isinstance(structure, Shape):
        render_shape(fig, structure, 0)
    elif isinstance(structure, Model):
        render_model(fig, structure)
    else:
        print("No type match")

    fig.update_layout(
        title="3D Origami Model",
        scene=dict(
            xaxis_title="Width",
            yaxis_title="Height",
            zaxis_title="Depth",
            aspectratio=dict(x=1, y=1, z=0.5),
        )
    )
    print("Done adding")
    fig.show()