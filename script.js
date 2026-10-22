"use strict";

const form = document.querySelector("#guess-form");
const guessInput = document.querySelector("#guess");
const checkButton = document.querySelector("#check-button");
const newButton = document.querySelector("#new-button");
const hint = document.querySelector("#hint");
const feedback = document.querySelector("#feedback");
const attemptsDisplay = document.querySelector("#attempts");
const rangeDisplay = document.querySelector("#range");

let secretNumber;
let attempts;
let lowestPossible;
let highestPossible;
let gameFinished;

function setFeedback(message, kind = "") {
  feedback.textContent = message;

  if (kind) {
    feedback.dataset.kind = kind;
  } else {
    delete feedback.dataset.kind;
  }
}

function newGame() {
  secretNumber = Math.floor(Math.random() * 100) + 1;
  attempts = 0;
  lowestPossible = 1;
  highestPossible = 100;
  gameFinished = false;

  guessInput.value = "";
  hint.textContent = "Hint: the number is between 1 and 100";
  setFeedback("A new number is ready. Make your first guess!");
  attemptsDisplay.textContent = "0";
  rangeDisplay.textContent = "1 - 100";
  checkButton.disabled = false;
  guessInput.focus();
}

function checkGuess(event) {
  event.preventDefault();

  if (gameFinished) {
    return;
  }

  const rawGuess = guessInput.value.trim();
  const guess = Number(rawGuess);

  if (rawGuess === "" || !Number.isInteger(guess)) {
    setFeedback("Please enter a whole number.", "error");
    guessInput.focus();
    return;
  }

  if (guess < 1 || guess > 100) {
    setFeedback("Your guess must be between 1 and 100.", "error");
    guessInput.focus();
    return;
  }

  attempts += 1;

  if (guess < secretNumber) {
    lowestPossible = Math.max(lowestPossible, guess + 1);
    setFeedback("Too low! Try a higher number.", "low");
  } else if (guess > secretNumber) {
    highestPossible = Math.min(highestPossible, guess - 1);
    setFeedback("Too high! Try a lower number.", "high");
  } else {
    setFeedback(
      `Correct! You found it in ${attempts} ${
        attempts === 1 ? "attempt" : "attempts"
      }!`,
      "win"
    );
    hint.textContent = `The secret number was ${secretNumber}`;
    gameFinished = true;
    checkButton.disabled = true;
  }

  if (!gameFinished) {
    hint.textContent = `Hint: ${lowestPossible} - ${highestPossible}`;
  }

  attemptsDisplay.textContent = String(attempts);
  rangeDisplay.textContent = `${lowestPossible} - ${highestPossible}`;
  guessInput.value = "";

  if (!gameFinished) {
    guessInput.focus();
  }
}

form.addEventListener("submit", checkGuess);
newButton.addEventListener("click", newGame);
newGame();
