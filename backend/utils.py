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

type_map = {
    "UNIT": ["MULTI_UNIT", "LAYER", "SHAPE", "MODEL"],
    "MULTI_UNIT": ["LAYER", "SHAPE", "MODEL"],
    "LAYER": ["SHAPE", "MODEL"],
    "SHAPE": ["MODEL"],
    "MODEL": [],
    "NUMBER": [],
    "BOOLEAN": [],
    "FUNCTION": []
}

class Scope:
    def __init__(self, name, parent=None):
        self.name = name
        self.variables = {}
        self.parent = parent
        self.children = []

    def __str__(self):
        children_names = [child.name for child in self.children]
        return f"Name: {self.name}\nVars: {self.variables}\nChildren: {children_names}"


    def declare(self, name, type, line, value=None):
        self.variables[name] = {}
        self.variables[name]["name"] = name
        self.variables[name]["type"] = type
        self.variables[name]["line"] = line
        self.variables[name]["value"] = value

    def get_type(self, name):
        if name in self.variables:
            return self.variables[name]["type"]
        elif self.parent:
            return self.parent.get_type(name)
        else:
            return None
        
    def get_line(self, name):
        return self.variables[name]["line"]
    
    def get_child(self, name):
        scope = self
        while scope is not None:
            for c in scope.children:
                if c.name == name:
                    return c
            scope = scope.parent
        return None
    
class ActivationRecord:
    def __init__(self, name, type_, nesting_level):
        self.name = name
        self.type = type_
        self.nesting_level = nesting_level
        self.members = {}

    def set(self, name, value):
        self.members[name] = value

    def get(self, name):
        return self.members.get(name)

class CallStack:
    def __init__(self):
        self.records = []

    def push(self, ar):
        self.records.append(ar)

    def pop(self):
        return self.records.pop()

    def peek(self, up=0):
        if up >= len(self.records):
            up = len(self.records)-1
        return self.records[-1-up]

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
    print("Generating figure...")
    fig.write_html("out.html")
    return fig.to_json()