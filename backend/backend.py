from fastapi import FastAPI, WebSocket
import asyncio
import json
import plotly.graph_objects as go
from main_backend import EvalVisitor

app = FastAPI()
interpreter = EvalVisitor()
clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    program = await websocket.receive_text()
    output = interpreter.interpret(program)
    print(f"Interpreter output: {output}")
    figure_json = json.loads(output)
    await websocket.send_text(json.dumps(figure_json))