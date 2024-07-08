import { useState } from "react";

import Header from "./components/Header";
import UserInput from "./components/UserInput";
import Results from "./components/Results";

function App() {
  const [userInput, setUserInput] = useState({
    initialInvestment: 10000,
    annualInvestment: 1200,
    expectedReturn: 6,
    duration: 10,
  });

  function handleChange(inputIdentifier, newValue) {
    setUserInput((prevState) => {
      return {
        ...prevState,
        [inputIdentifier]: +newValue,
      };
    });
  }

  const inputisValid =
    userInput.initialInvestment > 0 &&
    userInput.annualInvestment > 0 &&
    userInput.expectedReturn > 0 &&
    userInput.duration > 0;

  return (
    <>
      <Header />;
      <UserInput userInput={userInput} onChange={handleChange} />;
      {!inputisValid && (
        <p className="center">Please enter a duration greater than zero.</p>
      )}
      {inputisValid && <Results input={userInput} />};
    </>
  );
}

export default App;
