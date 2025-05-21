import React, { useState, useEffect, useRef } from "react";
import Plot from "react-plotly.js";
import "./App.css";

const WebSocketURL = "ws://localhost:8000/ws";
const API_URL = "http://localhost:8000";

export default function App() {
  const [figData, setFigData] = useState([]);
  const [layout, setLayout] = useState({});
  const [showPlot, setShowPlot] = useState(false);
  const [loading, setLoading] = useState(false);
  const [code, setCode] = useState("");
  const [showInfo, setShowInfo] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [showFileBrowser, setShowFileBrowser] = useState(false);
  const [programFiles, setProgramFiles] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileContent, setFileContent] = useState("");
  const [lineCount, setLineCount] = useState(1);
  const [textOutput, setTextOutput] = useState("");
  const textareaRef = useRef(null);
  const lineNumbersRef = useRef(null);

  useEffect(() => {
    if (showFileBrowser) {
      fetchProgramFiles();
    }
  }, [showFileBrowser]);

  useEffect(() => {
    const lines = code.split("\n").length;
    setLineCount(Math.max(lines, 1));
  }, [code]);

  useEffect(() => {
    const handleResize = () => {
      if (textareaRef.current && lineNumbersRef.current) {
        handleScroll();
      }
    };

    handleResize();

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, [lineCount]);

  const fetchProgramFiles = async () => {
    try {
      const response = await fetch(`${API_URL}/api/programs`);
      const data = await response.json();
      setProgramFiles(data.files || []);
    } catch (error) {
      console.error("Error fetching program files:", error);
      setErrorMessage("Failed to fetch program files");
    }
  };

  const fetchFileContent = async (filename) => {
    try {
      const response = await fetch(`${API_URL}/api/programs/${filename}`);
      const data = await response.json();

      if (data.error) {
        setErrorMessage(data.error);
        return;
      }

      setSelectedFile(filename);
      setFileContent(data.content);
    } catch (error) {
      console.error("Error fetching file content:", error);
      setErrorMessage("Failed to fetch file content");
    }
  };

  const loadFileToEditor = () => {
    if (fileContent) {
      setCode(fileContent);
      const lines = fileContent.split("\n").length;
      setLineCount(Math.max(lines, 1));
      setShowFileBrowser(false);
    }
  };

  const toggleFileBrowser = () => {
    setShowFileBrowser(!showFileBrowser);
  };

  const fetchFigure = () => {
    const ws = new WebSocket(WebSocketURL);

    ws.onopen = () => {
      setLoading(true);
      ws.send(code);
    };

    ws.onmessage = (event) => {
      const response = JSON.parse(event.data);

      if (response.type === "error") {
        setErrorMessage(response.message);
        setLoading(false);
        return;
      }

      if (response.type === "figure") {
        setLayout(response.layout);
        setFigData(response.data);
        setShowPlot(true);
      } else if (response.type === "text") {
        setTextOutput((prev) => prev + response.content + "\n");
      }

      setLoading(false);
    };

    ws.onerror = (err) => console.error("WebSocket Error:", err);
    ws.onclose = () => console.log("WebSocket closed");
  };

  const toggleInfo = () => {
    setShowInfo(!showInfo);
  };

  const handleScroll = () => {
    if (textareaRef.current && lineNumbersRef.current) {
      lineNumbersRef.current.scrollTop = textareaRef.current.scrollTop;
    }
  };

  const renderLineNumbers = () => {
    const numbers = [];
    for (let i = 1; i <= lineCount; i++) {
      numbers.push(
        <div key={i} className="line-number">
          {i}
        </div>
      );
    }
    return numbers;
  };

  const handleKeyDown = (e) => {
    if (e.key === "Tab") {
      e.preventDefault();

      const start = e.target.selectionStart;
      const end = e.target.selectionEnd;

      if (start !== end) {
        const selectedText = code.substring(start, end);
        const selectedLines = selectedText.split("\n");

        let newText;
        if (e.shiftKey) {
          const outdentedLines = selectedLines.map((line) =>
            line.startsWith("\t") ? line.substring(1) : line
          );
          newText = outdentedLines.join("\n");

          const numTabsRemoved = selectedLines.filter((line) =>
            line.startsWith("\t")
          ).length;

          const updatedCode =
            code.substring(0, start) + newText + code.substring(end);
          setCode(updatedCode);

          setTimeout(() => {
            e.target.selectionStart = start;
            e.target.selectionEnd = end - numTabsRemoved;
          }, 0);
        } else {
          const indentedLines = selectedLines.map((line) => "\t" + line);
          newText = indentedLines.join("\n");

          const updatedCode =
            code.substring(0, start) + newText + code.substring(end);
          setCode(updatedCode);

          setTimeout(() => {
            e.target.selectionStart = start;
            e.target.selectionEnd = end + selectedLines.length;
          }, 0);
        }
      } else {
        const newText = code.substring(0, start) + "\t" + code.substring(end);

        setCode(newText);

        setTimeout(() => {
          e.target.selectionStart = e.target.selectionEnd = start + 1;
        }, 0);
      }
    }
  };

  return (
    <div className="container">
      {errorMessage && (
        <div className="error-banner">
          {errorMessage}
          <button className="close-error" onClick={() => setErrorMessage("")}>
            ✖
          </button>
        </div>
      )}

      <div className="plot-container">
        {loading && <div className="loading-spinner"></div>}
        {showPlot && <Plot data={figData} layout={layout} className="plot" />}
        {textOutput && (
          <div className="output-container">
            <h3>Output:</h3>
            <pre className="text-output">{textOutput}</pre>
            <button
              className="clear-output-button"
              onClick={() => setTextOutput("")}
            >
              Clear Output
            </button>
          </div>
        )}
      </div>

      <div className="editor-container">
        <h3>Enter code to generate 3d origami model:</h3>
        <div className="code-editor-wrapper">
          <div className="line-numbers" ref={lineNumbersRef}>
            {renderLineNumbers()}
          </div>
          <textarea
            ref={textareaRef}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            onScroll={handleScroll}
            onKeyDown={handleKeyDown}
            className="code-editor"
            placeholder="Write your code here..."
          />
        </div>
        <div className="button-container">
          <button onClick={fetchFigure} className="button">
            Render Figure
          </button>
          <button onClick={toggleInfo} className="button">
            Info
          </button>
          <button onClick={toggleFileBrowser} className="button">
            Browse Examples
          </button>
        </div>
      </div>

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
              <span className="Heading">Variable declaration:</span>
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

      {showFileBrowser && (
        <div className="info-window show">
          <button className="close-info-button" onClick={toggleFileBrowser}>
            X
          </button>
          <div className="info-content">
            <h3>Example Programs</h3>
            <div className="file-list">
              {programFiles.length > 0 ? (
                programFiles.map((file) => (
                  <div
                    key={file}
                    className={`file-item ${
                      selectedFile === file ? "selected" : ""
                    }`}
                    onClick={() => fetchFileContent(file)}
                  >
                    {file}
                  </div>
                ))
              ) : (
                <p>No example files found</p>
              )}
            </div>
            {selectedFile && (
              <div className="file-preview">
                <h4>{selectedFile}</h4>
                <pre className="info-content">{fileContent}</pre>
                <button onClick={loadFileToEditor} className="load-file-button">
                  Load to Editor
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
