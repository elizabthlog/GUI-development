import random
import tkinter as tk

root = tk.Tk()
root.title("Eliza's Number Guessing Game")
root.geometry("500x700")
root.configure(background="#fca9a9")

attempts = 0
snumber = 0

def newgame():
    global snumber, attempts
    snumber  = random.randint(1, 20)
    attempts = 0

    message.config(text="Guess the number (1-20)")
    hint.config(text="")
    attempts_label.config(text="Attempts: 0")


def guess(number):
    global attempts
    attempts += 1

    attempts_label.config(text=f"Attempts: {attempts}")

    if number == snumber:
        message.config(text=f"Correct! It was {snumber}")
        hint.config(text="Starting new game...")
        root.after(1000, newgame)
        
    elif number < snumber:
        hint.config(text="Higher!")
    else:
        hint.config(text="Lower!")



title = tk.Label(
        root,
        text = "ELIZA'S GUESSING GAME",
        font = ("Poppins", 22, "bold"),
        bg="#fca9a9",
        fg = "white"
    )
title.pack(pady=15)


message = tk.Label(
    root,
    text = "Guess the number (1-20)",
    font = ("Arial", 16, "bold"),
    bg = "#fca9a9",
    fg ="#00f8c6"
)
message.pack(pady=10)

hint = tk.Label(
    root,
    text = "",
    font =("Arial", 14,"bold"),
    bg="#fca9a9",
    fg="#ff3300"
)
hint.pack(pady = 10)


attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 14, "bold"),
    bg="#fca9a9",
    fg="#ffffff"
)
attempts_label.pack(pady = 5)



frame = tk.Frame(
    root,
    bg = "#86b869",
)
frame.pack(pady = 25)



def on_enter(e):
    e.widget["background"] = "#ff66aa"

def on_leave(e):
    e.widget["background"] = "#ff3891"



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

    btn.grid(row=(i-1)//5, column=(i-1)%5, padx=6, pady=6)



newgame()

root.mainloop()  