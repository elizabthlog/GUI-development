import random
import tkinter as tk

# Window
root = tk.Tk()
root.title("Eliza's Number Guessing Game")
root.geometry("500x700")
root.configure(background="#fca9a9")

# Game variables
attempts = 0
snumber = 0
best_score = 999

# Load best score from file
try:
    with open("bestscore.txt", "r") as file:
        best_score = int(file.read())

except:
    best_score = 999

# Start / reset game
def newgame():
    global snumber, attempts

    snumber = random.randint(1, 20)
    attempts = 0

    message.config(text="Guess the number (1-20)")
    hint.config(text="")
    attempts_label.config(text="Attempts: 0")

# Check guesses
def guess(number):

    global attempts
    global best_score

    attempts += 1

    attempts_label.config(text=f"Attempts: {attempts}")

    # Correct guess
    if number == snumber:

        # Save best score
        if attempts < best_score:
            best_score = attempts

            with open("bestscore.txt", "w") as file:
                file.write(str(best_score))

            best_label.config(
                text=f"Best Score: {best_score}"
            )

        message.config(
            text=f"🎉 Correct! It was {snumber}"
        )

        hint.config(text="Starting new game...")

        # Restart after 1 second
        root.after(1000, newgame)

    # Too low
    elif number < snumber:
        hint.config(text="⬆ Higher!")

    # Too high
    else:
        hint.config(text="⬇ Lower!")

# Title
title = tk.Label(
    root,
    text="ELIZA'S GUESSING GAME",
    font=("Poppins", 22, "bold"),
    bg="#fca9a9",
    fg="white"
)
title.pack(pady=15)

# Main message
message = tk.Label(
    root,
    text="Guess the number (1-20)",
    font=("Arial", 16, "bold"),
    bg="#fca9a9",
    fg="#00f8c6"
)
message.pack(pady=10)

# Hint label
hint = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#fca9a9",
    fg="#ff3300"
)
hint.pack(pady=10)

# Attempts label
attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 14, "bold"),
    bg="#fca9a9",
    fg="white"
)
attempts_label.pack(pady=5)

# Best score label
best_label = tk.Label(
    root,
    text=f"Best Score: {best_score}",
    font=("Arial", 14, "bold"),
    bg="#fca9a9",
    fg="#00ffcc"
)
best_label.pack(pady=5)

# Button frame
frame = tk.Frame(
    root,
    bg="#fca9a9"
)
frame.pack(pady=25)

# Hover effects
def on_enter(e):
    e.widget["background"] = "#ff66aa"

def on_leave(e):
    e.widget["background"] = "#ff3891"

# Number buttons
for i in range(1, 21):

    btn = tk.Button(
        frame,
        text=str(i),
        width=5,
        height=2,
        font=("Arial", 12, "bold"),
        bg="#ff3891",
        fg="white",
        activebackground="#fca9a9",
        relief="raised",
        bd=4,
        command=lambda num=i: guess(num)
    )

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    btn.grid(
        row=(i-1)//5,
        column=(i-1)%5,
        padx=6,
        pady=6
    )

# Start game
newgame()

# Run window
root.mainloop()