from fastapi import FastAPI, WebSocket
import asyncio
import json
import plotly.graph_objects as go
from main import evaluate_expression
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    program = await websocket.receive_text()
    output = evaluate_expression(program)

    if isinstance(output, dict):
        await websocket.send_text(json.dumps(output))
    else:
        text, render, diagnostic_logs = output  # Modified to receive diagnostic logs
        
        # Send diagnostic logs first
        for log in diagnostic_logs:
            await websocket.send_text(json.dumps({
                "type": "diagnostic",
                "content": log
            }))
        
        # Send text output if any
        if text and len(text) > 0:
            await websocket.send_text(json.dumps({
                "type": "text",
                "content": "\n".join(text)
            }))
        
        # Send render output if any
        if render and render.strip():
            figure_json = json.loads(render)
            await websocket.send_text(json.dumps({
                "type": "figure",
                "data": figure_json["data"],
                "layout": figure_json["layout"]
            }))

@app.get("/api/programs")
async def list_programs():
    """List all text files in the programs directory"""
    programs_dir = os.path.join(os.path.dirname(__file__), "programs")
    files = [f for f in os.listdir(programs_dir) if f.endswith('.txt')]
    return {"files": files}

@app.get("/api/programs/{filename}")
async def get_program(filename: str):
    """Get the content of a specific text file"""
    programs_dir = os.path.join(os.path.dirname(__file__), "programs")
    file_path = os.path.join(programs_dir, filename)
    
    if not os.path.exists(file_path) or not filename.endswith('.txt'):
        return {"error": "File not found or invalid"}
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return {"filename": filename, "content": content}
