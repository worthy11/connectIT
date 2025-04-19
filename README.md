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
UNIT r = *red*
UNIT g = *green*
UNIT b = *blue*

LAYER first = r * 3
LAYER second = g * 2
LAYER third = b * 1

SHAPE pyramid
first <- second <- third --> pyramid

SHOW pyramid
```

## 🔺Setup

### Installing Dependencies

Ensure you have Python and all the required dependencies installed:

```
pip install -r requirements.txt
cd frontend
npm install vite plotly.js-dist react-plotly.js
```

### Running Web App

To run the web application, execute the following commands in two separate terminals:
First terminal:

```
cd backend
uvicorn backend:app --reload
```

Second terminal:

```
cd frontend
npm run dev
```

Then, visit the address `npm` gives you (usually [localhost at port 5137](http://localhost:5173/))

### Running Samples

Check out the `backend/programs/` directory. Choose a sample program you want to run and pass the name as a console argument to `main.py`, for example:

```
cd backend
py main.py shape_showcase.txt
```

Your figure can be viewed by opening `out.html` in the browser.
