import random
import tkinter as tk

root = tk.Tk()
root.title("Eliza's Number Guessing Game")
root.geometry("500x500")
root.configure(background="#a4c330")
root.mainloop()

attempts = 0
snumber = 0

def newgame():
    global snumber, attempts
    snumber  = random.randint(1.20)
    attempts = 0

    message.config(text="Guess the number (1-20)")
    hint.config(text="")
    attempts_label.config(text="Attempts: 0")


def guess(number);
    global attempts
    attempts += 1

    attempts_label.config(text=f"Attempts: {attempts}")

    if number == snumber:
        message.config(text=f"Correct! It was {snumber}")
        hint.config(text="Starting new game...")
        root.after(1000, new_game)
        
    elif number < snumber:
        hint.config(text="Higher!")
    else:
        hint.config(text="Lower!")



    title = tk.Label(
        root,
        text = "ELIZA'S GUESSING GAME",
        font = ("Poppins", 22, "bold"),
        bg="#a4c330",
        fg = "white"
    )
title.pack(pady=15)


message = tk.Label(
    root,
    text = "Guess the number (1-20)",
    font = ("Poppins", 16, "bold"),
    bg = "#a4c330",
    fg ="#00ffcc"
)


hint = tk.Label(
    root,
    text = "",
    font =("Poppins", 14,"bold"),
    bg="#1e1e2f",
    fg="#ffcc00"
)
hint.pack(pady = 10)


attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
attempts_label.pack(pady = 5)



frame = tk.Frame(
    root,
    bg = "#1e1e2f"',
)
attempts_label.pack(pady = 20)



def on_enter(e):
    e.widget["background"] = "#ff66aa"

def on_leave(e):
    e.widget["background"] = "#ff3399"


new_game()

root.mainloop()  