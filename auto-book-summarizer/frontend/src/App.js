
import React, { useState } from "react";
import axios from "axios";

const API = "http://<load-balancer-dns>/upload";

function App() {
  const [file, setFile] = useState(null);
  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post(API, formData);
    alert("Uploaded!");
  };
  return (
    <div className="App">
      <h1>Auto Book Summarizer</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default App;
