import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";

const WebSocketURL = "ws://localhost:8000/ws"; // Adjust for deployment

export default function App() {
  const [code, setCode] = useState(""); // User input code
  const [figures, setFigures] = useState([]); // List of units

  useEffect(() => {
    const ws = new WebSocket(WebSocketURL);
    ws.onmessage = (event) => {
      const figure = JSON.parse(event.data);
      setFigures((prev) => [...prev, figure]); // Add unit to scene
    };
    return () => ws.close();
  }, []);

  const handleInterpret = () => {
    setFigures([]); // Clear previous figures
    const ws = new WebSocket(WebSocketURL);
    ws.onopen = () => ws.send(code); // Send code to backend
  };

  return (
    <div>
      <textarea value={code} onChange={(e) => setCode(e.target.value)} />
      <button onClick={handleInterpret}>Interpret</button>
      <div>
        {figures.map((fig, index) => (
          <Plot key={index} data={fig.data} layout={fig.layout} />
        ))}
      </div>
    </div>
  );
}
