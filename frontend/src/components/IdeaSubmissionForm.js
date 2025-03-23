import React, { useState } from "react";

const IdeaSubmissionForm = ({ onEvaluate }) => {
  const [idea, setIdea] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [evaluationResult, setEvaluationResult] = useState(null);

  const handleChange = (e) => {
    setIdea(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/evaluate-idea/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ idea }),
      });

      const data = await response.json();
      if (response.ok) {
        setEvaluationResult(data);
        if (onEvaluate) onEvaluate(data);
      } else {
        throw new Error(data.error || "Failed to evaluate idea");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100 bg-dark text-white">
      <div className="card p-4 shadow-lg" style={{ width: "40rem" }}>
        <h2 className="text-center text-primary">Submit Your Startup Idea</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <textarea
              className="form-control"
              rows="5"
              value={idea}
              onChange={handleChange}
              placeholder="Describe your startup idea..."
              required
            />
          </div>
          <button type="submit" className="btn btn-primary w-100" disabled={loading}>
            {loading ? "Evaluating..." : "Submit Idea"}
          </button>
        </form>

        {error && <p className="text-danger mt-3">{error}</p>}

        {evaluationResult && (
          <div className="mt-4">
            <h4 className="text-success">Evaluation Results</h4>
            <p><strong>Feasibility Score:</strong> {evaluationResult.feasibilityScore}</p>
            <p><strong>Suggestions:</strong> {evaluationResult.suggestions}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default IdeaSubmissionForm;
