import "./App.css";
import Contributor from "./Contributor.jsx";
import contributors from "./Contributors.json";

function App() {
  return (
    <div className="app">
      <h1 className="heading">Contributors</h1>
      <div className="contributors-container">
        {contributors.contributors.map((contributor, index) => (
          <Contributor
            key={index}
            name={contributor.name}
            description={contributor.description}
            socialLink={contributor.githubLink}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
