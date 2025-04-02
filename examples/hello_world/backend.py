from fastapi import FastAPI, WebSocket
import asyncio
import json
import plotly.graph_objects as go
from interpreter import EvalVisitor  # Your interpreter

app = FastAPI()

# Active WebSocket connections
clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()  # Receive code from frontend
            await interpret_code(data, websocket)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        clients.remove(websocket)

async def interpret_code(code: str, websocket: WebSocket):
    interpreter = ConnectITInterpreter()
    output = interpreter.run(code)  # Your interpreter logic

    for unit in output:  # Send each unit separately
        figure = generate_plotly_figure(unit)
        await websocket.send_text(json.dumps(figure))
        await asyncio.sleep(0.5)  # Delay for animation effect

def generate_plotly_figure(unit):
    """ Generate 3D Plotly figure for a unit """
    fig = go.Figure()
    # Add the unit's triangular prism mesh here...
    return fig.to_json()
