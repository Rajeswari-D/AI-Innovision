import React, { useState } from "react";
import IdeaSubmissionForm from "./components/IdeaSubmissionForm";
import IdeaEvaluationResult from "./components/IdeaEvaluationResult";
import IdeaList from "./components/IdeaList";
import "./styles/App.css"; // ✅ Importing the CSS file

function App() {
  const [submittedIdeas, setSubmittedIdeas] = useState([]);
  const [evaluation, setEvaluation] = useState(null);

  const handleIdeaSubmit = async (idea) => {
    setSubmittedIdeas([...submittedIdeas, idea]);

    try {
      const response = await fetch("http://localhost:8000/evaluate-idea/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ idea }), // Fixed structure to send data properly
      });

      const data = await response.json();
      setEvaluation(data);
    } catch (error) {
      console.error("Error submitting idea:", error);
    }
  };

  return (
    <div className="app-container">
      <h1 className="text-center text-primary">Innovision AI Startup Idea Evaluator</h1>
      <div className="content-wrapper">
        <IdeaSubmissionForm onSubmit={handleIdeaSubmit} />
        <IdeaEvaluationResult evaluationData={evaluation} />
        <IdeaList ideas={submittedIdeas} />
      </div>
    </div>
  );
}

export default App;
