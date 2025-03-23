import React, { useState } from "react";
import { Card, Button, Container } from "react-bootstrap";
import "../styles/result.css"; // Importing the styles

const IdeaEvaluationResult = ({ evaluationData }) => {
  const [showSuggestions, setShowSuggestions] = useState(false);

  if (!evaluationData) return null;

  return (
    <Container className="result-container">
      <Card className="result-card">
        <Card.Body>
          <h3 className="text-primary">Evaluation Results</h3>
          <hr />

          {/* Feasibility Score */}
          <h4>Feasibility Score:</h4>
          <div className="feasibility-score">
            {evaluationData.feasibilityScore} / 100
          </div>

          {/* Toggle Button for Suggestions */}
          <Button
            className="suggestions-btn"
            variant="primary"
            onClick={() => setShowSuggestions(!showSuggestions)}
          >
            {showSuggestions ? "Hide Suggestions" : "Show Suggestions"}
          </Button>

          {/* Suggestions Section */}
          {showSuggestions && (
            <div className="suggestions-box">
              <h5>Suggestions:</h5>
              <p>{evaluationData.suggestions}</p>
            </div>
          )}
        </Card.Body>
      </Card>
    </Container>
  );
};

export default IdeaEvaluationResult;
