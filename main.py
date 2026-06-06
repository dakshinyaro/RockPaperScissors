import tkinter as tk
import random

# -----------------------------
# Create Main Window
# -----------------------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.resizable(False, False)

# -----------------------------
# Variables
# -----------------------------
choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="🎮 Rock Paper Scissors",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# -----------------------------
# Result Label
# -----------------------------
result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 14),
    justify="center"
)
result_label.pack(pady=20)

# -----------------------------
# Play Function
# -----------------------------
def play(user_choice):
    global player_score
    global computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        player_score += 1

    else:
        result = "💻 Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"""
Your Choice : {user_choice}

Computer Choice : {computer_choice}

{result}

----------------------------

Your Score : {player_score}

Computer Score : {computer_score}
"""
    )

# -----------------------------
# Reset Function
# -----------------------------
def reset_game():
    global player_score
    global computer_score

    player_score = 0
    computer_score = 0

    result_label.config(
        text="Choose Rock, Paper or Scissors"
    )

# -----------------------------
# Buttons
# -----------------------------
rock_btn = tk.Button(
    root,
    text="🪨 Rock",
    width=20,
    font=("Arial", 12),
    command=lambda: play("Rock")
)
rock_btn.pack(pady=5)

paper_btn = tk.Button(
    root,
    text="📄 Paper",
    width=20,
    font=("Arial", 12),
    command=lambda: play("Paper")
)
paper_btn.pack(pady=5)

scissors_btn = tk.Button(
    root,
    text="✂️ Scissors",
    width=20,
    font=("Arial", 12),
    command=lambda: play("Scissors")
)
scissors_btn.pack(pady=5)

reset_btn = tk.Button(
    root,
    text="🔄 Reset Score",
    width=20,
    font=("Arial", 12),
    command=reset_game
)
reset_btn.pack(pady=20)

# -----------------------------
# Run Application
# -----------------------------
root.mainloop()