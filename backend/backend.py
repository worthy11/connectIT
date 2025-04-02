from fastapi import FastAPI, WebSocket
import asyncio
import json
import plotly.graph_objects as go
from main_backend import EvalVisitor  # Your interpreter

app = FastAPI()
interpreter = EvalVisitor()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    output = interpreter.sample_render()  # Your interpreter logic
    figure_json = json.loads(output)
    # print("Sent JSON:", json.dumps(figure_json, indent=2))
    await websocket.send_text(json.dumps(figure_json))