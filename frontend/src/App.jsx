import React, { useState } from "react";
import Plot from "react-plotly.js";

const WebSocketURL = "ws://localhost:8000/ws";

export default function App() {
  const [figData, setFigData] = useState([]); // Stores traces (elements)
  const [layout, setLayout] = useState({}); // Stores layout
  const [showPlot, setShowPlot] = useState(false); // Controls rendering

  const fetchFigure = () => {
    setFigData([]); // Clear previous data
    setShowPlot(true);

    const ws = new WebSocket(WebSocketURL);
    ws.onmessage = (event) => {
      const figJson = JSON.parse(event.data);
      setLayout(figJson.layout); // Set layout once
      // animateElements(figJson.data);
      setFigData(figJson.data);
    };

    ws.onerror = (err) => console.error("WebSocket Error:", err);
    ws.onclose = () => console.log("WebSocket closed");
  };

  const animateElements = (data) => {
    let index = 0;
    const interval = setInterval(() => {
      if (index < data.length) {
        setFigData((prev) => [...prev, data[index]]);
        index++;
      } else {
        clearInterval(interval);
      }
    }, 1);
  };

  return (
    <div>
      <button onClick={fetchFigure}>Render Figure</button>
      {showPlot && <Plot data={figData} layout={layout} />}
    </div>
  );
}
