import React, { useState } from "react";
import Plot from "react-plotly.js";
import "./App.css";

const WebSocketURL = "ws://localhost:8000/ws";

export default function App() {
  const [figData, setFigData] = useState([]);
  const [layout, setLayout] = useState({});
  const [showPlot, setShowPlot] = useState(false);
  const [code, setCode] = useState("");
  const [showInfo, setShowInfo] = useState(false); // Nowy stan do kontrolowania widoczności okna Info

  const fetchFigure = () => {
    setFigData([]);
    setShowPlot(true);
    const ws = new WebSocket(WebSocketURL);
    ws.onmessage = (event) => {
      const figJson = JSON.parse(event.data);
      setLayout(figJson.layout);
      setFigData(figJson.data);
    };
    ws.onerror = (err) => console.error("WebSocket Error:", err);
    ws.onclose = () => console.log("WebSocket closed");
  };

  const toggleInfo = () => {
    setShowInfo(!showInfo); // Zmiana stanu widoczności okna z instrukcjami
  };

  return (
    <div className="container">
      {/* Left: Scatter Plot */}
      <div className="plot-container">
        {showPlot && <Plot data={figData} layout={layout} className="plot" />}
      </div>

      {/* Right: Code Editor */}
      <div className="editor-container">
        <h3>Enter code to generate 3d origami model:</h3>
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className="code-editor"
          placeholder="Write your code here..."
        />
        <div className="button-container">
          <button onClick={fetchFigure} className="render-button">
            Render Figure
          </button>
          <button onClick={toggleInfo} className="info-button">
            Info
          </button>
        </div>
      </div>

      {/* Info Window */}
      {showInfo && (
        <div className="info-window show">
          <button className="close-info-button" onClick={toggleInfo}>
            X
          </button>
          <div className="info-content">
            <h3>Instructions</h3>
            <p>Here you can add your instructions or information...</p>
          </div>
        </div>
      )}
    </div>
  );
}

