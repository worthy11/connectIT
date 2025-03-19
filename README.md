# 🔺connectIT🔺

connectIT is a domain-specific language designed for describing and visualizing 3D modular origami structures. With an intuitive syntax, it enables creators to define units, layers, and complex folded shapes programmatically. <br />

## 🔺Features
- Declarative Syntax – Define origami models using intuitive language constructs.
- Arithmetic & Logic Operations – Perform calculations and comparisons.
- Loops & Conditionals – Control structures for procedural generation.
- Functions & Recursion – Define reusable patterns.
- Real-time Visualization – Render 3D models using Plotly. <br />

## 🔺Example Code
```
LAYER first = UNIT(red) * 3;
LAYER second = UNIT(green) * 2;
LAYER third = UNIT(blue) * 1;

CONNECT second TO first;
MODE between;
SHIFT 0;

FORMS SHAPE pyramid;
CONNECT third EXTENDS pyramid;
```

## 🔺Setup
### Installing Dependencies

Ensure you have Python and ANTLR4 installed:

```
pip install antlr4-python3-runtime plotly
```

### Cloning the Repository

```
git clone https://github.com/worthy11/connectIT.git
cd connectIT
antlr4 -Dlanguage=Python3 connectIT.g4
```

### Running the Interpreter

```
python main.py examples/pyramid.fold
```

### Visualization
```py
# TODO
```
