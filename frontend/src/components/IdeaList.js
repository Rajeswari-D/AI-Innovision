import React from "react";

const IdeaList = ({ ideas }) => {
  return (
    <div className="idea-list">
      <h2>Submitted Ideas</h2>
      {ideas.length === 0 ? <p>No ideas submitted yet.</p> : (
        <ul>
          {ideas.map((idea, index) => (
            <li key={index}>
              <strong>{idea.title}</strong> - {idea.description}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default IdeaList;
