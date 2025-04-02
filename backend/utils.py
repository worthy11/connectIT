import plotly.graph_objects as go
import numpy as np

from data_types import *

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
        showlegend=False
    )
    fig.write_html("out.html")
    return fig.to_json()
    with open("fig.json", "w") as f:
        f.write(fig.to_json())