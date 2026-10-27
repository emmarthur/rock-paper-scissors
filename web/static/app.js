const winsEl = document.getElementById("wins");
const lossesEl = document.getElementById("losses");
const tiesEl = document.getElementById("ties");
const versusLine = document.getElementById("versus-line");
const countdownEl = document.getElementById("countdown");
const computerReveal = document.getElementById("computer-reveal");
const resultMessage = document.getElementById("result-message");
const errorEl = document.getElementById("error-text");
const resetBtn = document.getElementById("btn-reset");
const moveButtons = document.querySelectorAll(".move-btn");

const LABELS = { rock: "ROCK", paper: "PAPER", scissors: "SCISSORS" };

let score = { wins: 0, losses: 0, ties: 0 };
let busy = false;

function setError(message) {
  errorEl.hidden = !message;
  errorEl.textContent = message || "";
}

function renderScore() {
  winsEl.textContent = String(score.wins);
  lossesEl.textContent = String(score.losses);
  tiesEl.textContent = String(score.ties);
}

function setMovesDisabled(disabled) {
  moveButtons.forEach((btn) => {
    btn.disabled = disabled;
  });
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function clearArena() {
  countdownEl.hidden = true;
  countdownEl.textContent = "";
  computerReveal.hidden = true;
  computerReveal.textContent = "";
  resultMessage.hidden = true;
  resultMessage.textContent = "";
  resultMessage.classList.remove("is-win", "is-lose", "is-tie");
}

async function playMove(move) {
  if (busy) return;
  busy = true;
  setMovesDisabled(true);
  setError(null);
  clearArena();

  versusLine.textContent = `${LABELS[move]} versus...`;

  let payload;
  try {
    const res = await fetch("/api/play", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ move, ...score }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || "Could not play round.");
    payload = data;
  } catch (err) {
    setError(err.message || "Could not play round.");
    versusLine.textContent = "Choose your move";
    busy = false;
    setMovesDisabled(false);
    return;
  }

  countdownEl.hidden = false;
  await sleep(500);
  countdownEl.textContent = "1...";
  await sleep(250);
  countdownEl.textContent = "2...";
  await sleep(250);
  countdownEl.textContent = "3...";
  await sleep(250);
  countdownEl.hidden = true;

  computerReveal.hidden = false;
  computerReveal.textContent = payload.computer_label;

  await sleep(500);

  resultMessage.hidden = false;
  resultMessage.textContent = payload.message;
  resultMessage.classList.add(`is-${payload.outcome === "win" ? "win" : payload.outcome === "lose" ? "lose" : "tie"}`);

  score = {
    wins: payload.wins,
    losses: payload.losses,
    ties: payload.ties,
  };
  renderScore();

  await sleep(400);
  versusLine.textContent = "Choose your move";
  clearArena();
  busy = false;
  setMovesDisabled(false);
}

moveButtons.forEach((btn) => {
  btn.addEventListener("click", () => playMove(btn.dataset.move));
});

resetBtn.addEventListener("click", async () => {
  if (busy) return;
  setError(null);
  try {
    const res = await fetch("/api/reset", { method: "POST" });
    const data = await res.json();
    score = data;
    renderScore();
    versusLine.textContent = "Choose your move";
    clearArena();
  } catch {
    setError("Could not reset score.");
  }
});

renderScore();
