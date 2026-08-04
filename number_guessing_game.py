import random
import tkinter as tk


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.root.geometry("520x460")
        self.root.resizable(False, False)
        self.root.configure(bg="#EAF2FF")

        self.secret_number = 0
        self.attempts = 0
        self.lowest_possible = 1
        self.highest_possible = 100
        self.game_finished = False

        self.guess_var = tk.StringVar()
        self.feedback_var = tk.StringVar()
        self.attempts_var = tk.StringVar()
        self.range_var = tk.StringVar()

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        tk.Label(
            self.root,
            text="Guess the Number",
            font=("Arial", 24, "bold"),
            bg="#EAF2FF",
            fg="#12355B"
        ).pack(pady=(28, 6))

        tk.Label(
            self.root,
            text="I have chosen a secret number from 1 to 100.",
            font=("Arial", 11),
            bg="#EAF2FF",
            fg="#456A8F"
        ).pack()

        card = tk.Frame(self.root, bg="white", padx=30, pady=25)
        card.pack(padx=42, pady=22, fill="both")

        tk.Label(
            card,
            textvariable=self.range_var,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#12355B"
        ).pack(pady=(0, 14))

        tk.Label(
            card,
            text="Enter your guess",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#12355B"
        ).pack(anchor="w")

        self.guess_entry = tk.Entry(
            card,
            textvariable=self.guess_var,
            font=("Arial", 15),
            justify="center",
            relief="solid",
            bd=1
        )
        self.guess_entry.pack(fill="x", pady=(6, 16), ipady=7)

        self.guess_button = tk.Button(
            card,
            text="Check Guess",
            command=self.check_guess,
            font=("Arial", 11, "bold"),
            bg="#2563EB",
            fg="#12355B",
            activebackground="white",
            activeforeground="#12355B",
            relief="flat",
            pady=9
        )
        self.guess_button.pack(fill="x")

        tk.Button(
            card,
            text="Start New Game",
            command=self.new_game,
            font=("Arial", 11, "bold"),
            bg="#DCE8F7",
            fg="#12355B",
            activebackground="#C9DBF1",
            relief="flat",
            pady=9
        ).pack(fill="x", pady=(10, 16))

        tk.Label(
            card,
            textvariable=self.feedback_var,
            font=("Arial", 12, "bold"),
            bg="#E8F1FF",
            fg="#12355B",
            wraplength=380,
            padx=12,
            pady=12
        ).pack(fill="x")

        tk.Label(
            card,
            textvariable=self.attempts_var,
            font=("Arial", 10),
            bg="white",
            fg="#456A8F"
        ).pack(pady=(15, 0))

        self.root.bind("<Return>", lambda event: self.check_guess())

    def check_guess(self):
        if self.game_finished:
            return

        try:
            guess = int(self.guess_var.get().strip())
        except ValueError:
            self.feedback_var.set("Please enter a whole number between 1 and 100.")
            return

        if guess < 1 or guess > 100:
            self.feedback_var.set("Your guess must be between 1 and 100.")
            return

        self.attempts += 1

        if guess < self.secret_number:
            self.lowest_possible = max(self.lowest_possible, guess + 1)
            self.feedback_var.set("Too low! Try a higher number.")
        elif guess > self.secret_number:
            self.highest_possible = min(self.highest_possible, guess - 1)
            self.feedback_var.set("Too high! Try a lower number.")
        else:
            self.feedback_var.set(
                f"Correct! You guessed the number in {self.attempts} attempts."
            )
            self.range_var.set(f"The secret number was {self.secret_number}.")
            self.game_finished = True
            self.guess_button.config(state=tk.DISABLED, bg="#94A3B8")

        if not self.game_finished:
            self.range_var.set(
                f"Hint: the number is between "
                f"{self.lowest_possible} and {self.highest_possible}."
            )

        self.attempts_var.set(f"Attempts: {self.attempts}")
        self.guess_var.set("")
        self.guess_entry.focus()

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.lowest_possible = 1
        self.highest_possible = 100
        self.game_finished = False

        self.guess_var.set("")
        self.range_var.set("Hint: the number is between 1 and 100.")
        self.feedback_var.set("A new secret number has been generated. Good luck!")
        self.attempts_var.set("Attempts: 0")
        self.guess_button.config(state=tk.NORMAL, bg="#2563EB")
        self.guess_entry.focus()


root = tk.Tk()
NumberGuessingGame(root)
root.mainloop()
