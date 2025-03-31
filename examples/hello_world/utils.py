from data_types import *
import plotly.graph_objects as go
import numpy as np

color_map = {
    "red": "rgb(255, 0, 0)",
    "green": "rgb(0, 255, 0)",
    "blue": "rgb(0, 0, 255)",
    "white": "rgb(255, 255, 255)",
    "black": "rgb(0, 0, 0)"
}

def render_model(fig, model: Model | list):
    for idx, shape in enumerate(model):
        shape.render(fig)

def show_figure(fig, structure: Structure):
    structure.render(fig)

    fig.update_layout(
        title="3D Origami Model",
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="data",
        ),
    )
    print("HERE")
    fig.write_html("out.html")

# r = Layer('a', [Unit('a', 'red', 'red')]*10, True, 0, 0)
# g = Layer('a', [Unit('a', 'green', 'red')]*10, True, 0, 1)
# b = Layer('a', [Unit('a', 'blue', 'red')]*10, True, 0, 0)
# s = Shape('a', [r, g, b])
# fig = go.Figure()
# show_figure(fig, s)