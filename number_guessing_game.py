```python
import random
import tkinter as tk


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("560x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#0F172A")

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

        # ---------------- HEADER ----------------

        header = tk.Frame(
            self.root,
            bg="#0F172A"
        )
        header.pack(fill="x", pady=(30, 5))

        tk.Label(
            header,
            text="NUMBER",
            font=("Arial", 12, "bold"),
            bg="#0F172A",
            fg="#38BDF8"
        ).pack()

        tk.Label(
            header,
            text="GUESSING GAME",
            font=("Arial", 28, "bold"),
            bg="#0F172A",
            fg="white"
        ).pack()

        tk.Label(
            header,
            text="Can you find the hidden number?",
            font=("Arial", 11),
            bg="#0F172A",
            fg="#94A3B8"
        ).pack(pady=(5, 0))

        # ---------------- MAIN CARD ----------------

        card = tk.Frame(
            self.root,
            bg="#1E293B",
            padx=35,
            pady=30
        )
        card.pack(
            padx=45,
            pady=25,
            fill="both"
        )

        # Range / Hint

        tk.Label(
            card,
            textvariable=self.range_var,
            font=("Arial", 12, "bold"),
            bg="#1E293B",
            fg="#38BDF8"
        ).pack(pady=(0, 25))

        # Input title

        tk.Label(
            card,
            text="ENTER YOUR GUESS",
            font=("Arial", 10, "bold"),
            bg="#1E293B",
            fg="#CBD5E1"
        ).pack()

        # Guess Entry

        self.guess_entry = tk.Entry(
            card,
            textvariable=self.guess_var,
            font=("Arial", 24, "bold"),
            justify="center",
            bg="#0F172A",
            fg="white",
            insertbackground="white",
            relief="flat",
            bd=0
        )

        self.guess_entry.pack(
            fill="x",
            pady=(8, 20),
            ipady=10
        )

        # Check Button

        self.guess_button = tk.Button(
            card,
            text="CHECK GUESS",
            command=self.check_guess,
            font=("Arial", 11, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=12
        )

        self.guess_button.pack(
            fill="x"
        )

        # New Game Button

        tk.Button(
            card,
            text="↻  NEW GAME",
            command=self.new_game,
            font=("Arial", 10, "bold"),
            bg="#334155",
            fg="#E2E8F0",
            activebackground="#475569",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=10
        ).pack(
            fill="x",
            pady=(10, 22)
        )

        # ---------------- FEEDBACK BOX ----------------

        feedback_frame = tk.Frame(
            card,
            bg="#0F172A",
            padx=15,
            pady=15
        )
        feedback_frame.pack(
            fill="x"
        )

        tk.Label(
            feedback_frame,
            textvariable=self.feedback_var,
            font=("Arial", 11, "bold"),
            bg="#0F172A",
            fg="#E2E8F0",
            wraplength=390
        ).pack()

        # ---------------- STATS ----------------

        stats = tk.Frame(
            card,
            bg="#1E293B"
        )
        stats.pack(
            fill="x",
            pady=(20, 0)
        )

        # Attempts

        attempts_box = tk.Frame(
            stats,
            bg="#0F172A",
            padx=15,
            pady=10
        )
        attempts_box.pack(
            side="left",
            expand=True,
            fill="x",
            padx=(0, 5)
        )

        tk.Label(
            attempts_box,
            text="ATTEMPTS",
            font=("Arial", 8, "bold"),
            bg="#0F172A",
            fg="#64748B"
        ).pack()

        tk.Label(
            attempts_box,
            textvariable=self.attempts_var,
            font=("Arial", 11, "bold"),
            bg="#0F172A",
            fg="white"
        ).pack()

        # Range

        range_box = tk.Frame(
            stats,
            bg="#0F172A",
            padx=15,
            pady=10
        )
        range_box.pack(
            side="left",
            expand=True,
            fill="x",
            padx=(5, 0)
        )

        tk.Label(
            range_box,
            text="RANGE",
            font=("Arial", 8, "bold"),
            bg="#0F172A",
            fg="#64748B"
        ).pack()

        self.range_stat = tk.Label(
            range_box,
            text="1 - 100",
            font=("Arial", 11, "bold"),
            bg="#0F172A",
            fg="white"
        )
        self.range_stat.pack()

        # Footer

        tk.Label(
            self.root,
            text="Press ENTER to check your guess",
            font=("Arial", 9),
            bg="#0F172A",
            fg="#64748B"
        ).pack(
            pady=(0, 15)
        )

        self.root.bind(
            "<Return>",
            lambda event: self.check_guess()
        )

    def check_guess(self):

        if self.game_finished:
            return

        try:
            guess = int(
                self.guess_var.get().strip()
            )

        except ValueError:
            self.feedback_var.set(
                "Please enter a whole number."
            )
            return

        if guess < 1 or guess > 100:
            self.feedback_var.set(
                "Your guess must be between 1 and 100."
            )
            return

        self.attempts += 1

        if guess < self.secret_number:

            self.lowest_possible = max(
                self.lowest_possible,
                guess + 1
            )

            self.feedback_var.set(
                "Too low! Try a higher number."
            )

        elif guess > self.secret_number:

            self.highest_possible = min(
                self.highest_possible,
                guess - 1
            )

            self.feedback_var.set(
                "Too high! Try a lower number."
            )

        else:

            self.feedback_var.set(
                f"Correct! You found it in "
                f"{self.attempts} attempts!"
            )

            self.range_var.set(
                f"The secret number was {self.secret_number}"
            )

            self.game_finished = True

            self.guess_button.config(
                state=tk.DISABLED,
                bg="#475569"
            )

        if not self.game_finished:

            self.range_var.set(
                f"Hint: {self.lowest_possible} - "
                f"{self.highest_possible}"
            )

        self.attempts_var.set(
            str(self.attempts)
        )

        self.range_stat.config(
            text=f"{self.lowest_possible} - "
                 f"{self.highest_possible}"
        )

        self.guess_var.set("")
        self.guess_entry.focus()

    def new_game(self):

        self.secret_number = random.randint(
            1,
            100
        )

        self.attempts = 0
        self.lowest_possible = 1
        self.highest_possible = 100
        self.game_finished = False

        self.guess_var.set("")

        self.range_var.set(
            "Hint: the number is between 1 and 100"
        )

        self.feedback_var.set(
            "A new number is ready. Make your first guess!"
        )

        self.attempts_var.set("0")

        self.range_stat.config(
            text="1 - 100"
        )

        self.guess_button.config(
            state=tk.NORMAL,
            bg="#2563EB"
        )

        self.guess_entry.focus()


# ---------------- START GAME ----------------

root = tk.Tk()

game = NumberGuessingGame(root)

root.mainloop()
```
