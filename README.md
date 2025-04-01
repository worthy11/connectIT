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
LAYER first = *red* * 3;
LAYER second = *green* * 2;
LAYER third = *blue* * 1;

SHAPE pyramid
first <- second <- third --> pyramid

SHOW pyramid
```

## 🔺Setup

### Installing Dependencies

Ensure you have Python and ANTLR4 installed:

```
pip install antlr4-python3-runtime antlr4-tools plotly
```

### Cloning the Repository

```
git clone https://github.com/worthy11/connectIT.git
```

### Running the Interpreter

Check out the `examples/` directory. After generating all necessary components, run one of the example interpreters:

```
py examples/antlr_demo/ExprInterpreter.py
```

See `examples/antlr_demo/README.md` for more instructions.

### Visualization

```py
# TODO
```
