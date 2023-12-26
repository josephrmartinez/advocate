import { useState } from "react"

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));


export default function RecordAppointment() {
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("/api/predictions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt: e.target.prompt.value,
      }),
    });
    let prediction = await response.json();
    if (response.status !== 201) {
      setError(prediction.detail);
      return;
    }
    setPrediction(prediction);

    while (
      prediction.status !== "succeeded" &&
      prediction.status !== "failed"
    ) {
      await sleep(1000);
      const response = await fetch("/api/predictions/" + prediction.id);
      prediction = await response.json();
      if (response.status !== 200) {
        setError(prediction.detail);
        return;
      }
      console.log({prediction})
      setPrediction(prediction);
    }
  };

    return (
      <div className="flex flex-col items-center">
        <form className="flex flex-col items-center" onSubmit={handleSubmit}>
          <div>upload recording</div>
          <input type="file" name="file"></input>
          <button type="submit">Upload and transcribe</button>
        </form>

      {error && <div>{error}</div>}

      {prediction && (
        <div>
            {prediction.output && (
              <div>
              {prediction.output}
              </div>
            )}
            <p>status: {prediction.status}</p>
        </div>
      )}  

      
      </div>
    )
  }
  