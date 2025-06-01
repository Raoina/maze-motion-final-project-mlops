async function getPredictedLabel(processed_t) {
  const response = await fetch("https://maze-motion-final-project-mlops-production.up.railway.app/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ features: processed_t }),
  });

  if (!response.ok) {
    console.error("API error:", response.statusText);
    return null;
  }

  const data = await response.json();
  console.log("Predicted gesture:", data.gesture);
  return data.gesture;  
}
