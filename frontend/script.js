alert("Script loaded");

function scan() {
  const text = document.getElementById("inputText").value.toLowerCase();

  let score = 0;
  let reasons = [];

  if (text.includes("urgent") || text.includes("immediately")) {
    score += 25;
    reasons.push("Urgency-based social engineering detected");
  }

  if (text.includes("verify") || text.includes("login") || text.includes("password")) {
    score += 30;
    reasons.push("Credential harvesting keywords found");
  }

  if (text.includes("http")) {
    score += 15;
    reasons.push("Contains external link");
  }

  if (text.match(/\.(xyz|top|tk|ru)/)) {
    score += 20;
    reasons.push("High-risk domain extension");
  }

  score = Math.min(score, 100);

  // UI updates
  const badge = document.getElementById("threatBadge");
  const bar = document.getElementById("barFill");
  const scoreText = document.getElementById("scoreText");
  const reasonsList = document.getElementById("reasons");
  const recommendation = document.getElementById("recommendation");

  badge.className = "badge";
  if (score >= 70) {
    badge.textContent = "HIGH";
    badge.classList.add("high");
    recommendation.textContent = "Do NOT click links or share sensitive information.";
  } else if (score >= 40) {
    badge.textContent = "MEDIUM";
    badge.classList.add("medium");
    recommendation.textContent = "Proceed with caution and verify the sender.";
  } else {
    badge.textContent = "LOW";
    badge.classList.add("low");
    recommendation.textContent = "No immediate action required.";
  }

  bar.style.width = score + "%";
  scoreText.textContent = `Risk Score: ${score} / 100`;

  reasonsList.innerHTML = "";
  reasons.forEach(r => {
    const li = document.createElement("li");
    li.textContent = r;
    reasonsList.appendChild(li);
  });
}
