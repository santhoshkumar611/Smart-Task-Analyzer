function analyzeTasks() {
  const input = document.getElementById("tasksInput").value;
  const strategy = document.getElementById("strategy").value;
  const resultDiv = document.getElementById("result");

  let tasks;
  try {
    tasks = JSON.parse(input);
  } catch (e) {
    alert("Invalid JSON format");
    return;
  }

  fetch(`http://127.0.0.1:8000/api/tasks/analyze/?strategy=${strategy}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(tasks)
  })
    .then(res => res.json())
    .then(data => {
      resultDiv.innerHTML = "";

      data.forEach(task => {
        let level = "low";
        if (task.score >= 7) level = "high";
        else if (task.score >= 4) level = "medium";

        const div = document.createElement("div");
        div.className = `task ${level}`;
        div.innerHTML = `
          <h3>${task.title}</h3>
          <p>Score: <strong>${task.score}</strong></p>
          <p>Due Date: ${task.due_date || "N/A"}</p>
          <p>Estimated Hours: ${task.estimated_hours || "-"}</p>
          <p>Importance: ${task.importance || "-"}</p>
        `;
        resultDiv.appendChild(div);
      });
    })
    .catch(() => {
      alert("Error connecting to backend");
    });
}
