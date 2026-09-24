# Guess the Number Game

A user-friendly desktop number guessing game built with **Python and Tkinter**. The program generates a random number between 1 and 100 and challenges the user to guess it.

This project was created for **SkillCraft Technology — Software Development Internship, Task 02**.

## Features

- Generates a random secret number between 1 and 100
- Accepts guesses from the user
- Displays whether the guess is too high or too low
- Narrows the possible-number range after each guess
- Tracks the number of attempts
- Validates invalid and out-of-range input
- Includes a **Start New Game** button
- Supports pressing the **Enter** key to check a guess
- Provides a simple and user-friendly graphical interface
- Built using Python's Tkinter library

## Technologies Used

- **Python**
- **Tkinter** — for the graphical user interface
- **Random** — for generating the secret number

## How to Run

### 1. Clone the Repository

Clone this repository to your computer:

```bash
git clone <your-repository-url>
```

### 2. Open the Project

Open the project folder in **VS Code** or your preferred code editor.

### 3. Open the Terminal

Navigate to the project directory:

```bash
cd SCT_SD_2
```

### 4. Run the Application

Run the following command:

```bash
python3 number_guessing_game.py
```

The game window will open automatically.

## How to Use

1. Start the application using the command above.
2. A secret number between **1 and 100** will be generated automatically.
3. Enter your guess in the input box.
4. Click **Check Guess** or press the **Enter** key.
5. The game will tell you whether your guess is:
   - **Too low** — try a higher number.
   - **Too high** — try a lower number.
   - **Correct** — you found the secret number.
6. Use the displayed range hint to narrow down your next guess.
7. The **Attempts** counter shows how many guesses you have made.
8. After winning, click **Start New Game** to generate a new secret number and play again.

## Input Validation

The game accepts only whole numbers between **1 and 100**.

If you enter:
- Letters or other invalid characters
- Decimal numbers
- A number below 1
- A number above 100

the game will display an appropriate error message.

## Project Structure

```text
SCT_SD_2/
├── number_guessing_game.py
├── README.md
└── .gitignore
```

## Example

```text
Secret Number: 57

Guess: 30
→ Too low! Try a higher number.

Guess: 80
→ Too high
