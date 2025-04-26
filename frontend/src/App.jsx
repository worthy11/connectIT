import React, { useState } from "react";
import Plot from "react-plotly.js";
import "./App.css";

const WebSocketURL = "ws://localhost:8000/ws";

export default function App() {
  const [figData, setFigData] = useState([]);
  const [layout, setLayout] = useState({});
  const [showPlot, setShowPlot] = useState(false);
  const [loading, setLoading] = useState(false);
  const [code, setCode] = useState("");
  const [showInfo, setShowInfo] = useState(false); // Nowy stan do kontrolowania widoczności okna Info
  const [errorMessage, setErrorMessage] = useState(""); // New state for error message

  const fetchFigure = () => {
    setFigData([]);
    const ws = new WebSocket(WebSocketURL);

    ws.onopen = () => {
      setLoading(true);
      ws.send(code);
    };

    ws.onmessage = (event) => {
      const response = JSON.parse(event.data);
    
      if (response.type === "error") {
        setErrorMessage(response.message); // Set error message
        setLoading(false);
        setShowPlot(false);
        return;
      }
    
      setLayout(response.layout);
      setFigData(response.data);
      setLoading(false);
      setShowPlot(true);
    };
    
    ws.onerror = (err) => console.error("WebSocket Error:", err);
    ws.onclose = () => console.log("WebSocket closed");
  };

  const toggleInfo = () => {
    setShowInfo(!showInfo); // Zmiana stanu widoczności okna z instrukcjami
  };

  return (
    <div className="container">
      {/* Error Banner */}
      {errorMessage && (
        <div className="error-banner">
          {errorMessage}
          <button className="close-error" onClick={() => setErrorMessage("")}>✖</button>
        </div>
      )}

      {/* Left: Scatter Plot */}
      <div className="plot-container">
        {/* Loading spinner */}
        {loading && <div className="loading-spinner"></div>}
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
            <span className="Heading2">Instructions:</span>
            <br />
            <p>
              <span className="Heading">Connection methods:</span>
              <br />
              A &lt;- B : connecting B on top of A<br />
              (one output to one input - horizontal connection)
              <br />
              <br />
              A &lt;&lt;- B : connecting B on top of A<br />
              (both outputs to both inputs - vertical connection)
              <br />
              <br />
              A &lt;-1- B : connection with a shift of 1 module
              <br />
              <br />
              A &lt;-/- B : disconnecting B from the top of A<br />
              <br />
              A -/-&gt; B : disconnecting A from the bottom of B<br />
              <br />
              A &lt;- B --&gt; C : assigning the result of the connection to C
              <br />
              <br />
              <span class="Heading">Variable declaration:</span>
              <br />
              <br />
              UNIT unit1, unit2, unit3
              <br />
              <br />
              LAYER first = unit1 * 3<br />
              LAYER second = unit2 * 2<br />
              LAYER third = unit3
              <br />
              <br />
              SHAPE pyramid
              <br />
              first &lt;- second &lt;- third --&gt; pyramid
              <br />
              <br />
              SHAPE flipped_pyramid
              <br />
              first &lt;-1- second &lt;-1- third --&gt; flipped_pyramid
              <br />
              <br />
              flipped_pyramid &lt;-/- third
              <br />
              first -/-&gt; flipped_pyramid
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
