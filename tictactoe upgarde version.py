import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to check winner
def check_winner():
    global winner, x_score, o_score, draw_score, games_played
    for combo in [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="#4CAF50", fg="white")  # Green highlight
            messagebox.showinfo("Tic Tac Toe", f"🎉 Player {buttons[combo[0]]['text']} wins this round!")
            winner = True
            if buttons[combo[0]]["text"] == "X":
                x_score += 1
            else:
                o_score += 1
            games_played += 1
            update_scoreboard()
            check_series_end()
            return
    
    # Check for draw
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic Tac Toe", "😮 It's a Draw!")
        draw_score += 1
        winner = True
        games_played += 1
        update_scoreboard()
        check_series_end()


# Function for button click
def button_click(index):
    global current_player, winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()


# Toggle between players
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    status_label.config(text=f"Player {current_player}'s turn")


# Restart the current board (new round)
def restart_game():
    global current_player, winner
    winner = False
    status_label.config(text=f"Player {current_player}'s turn")
    for button in buttons:
        button.config(text="", bg="#ECECEC", fg="black")


# Exit game
def exit_game():
    root.quit()


# Update scoreboard
def update_scoreboard():
    score_label.config(
        text=f"❌ X: {x_score}   ⭕ O: {o_score}   🤝 Draws: {draw_score}   | Round {games_played+1}/{total_games}"
    )


# Check if series ended
def check_series_end():
    global games_played, total_games
    if games_played >= total_games:
        if x_score > o_score:
            final_winner = "❌ Player X is the Final Winner!"
        elif o_score > x_score:
            final_winner = "⭕ Player O is the Final Winner!"
        else:
            final_winner = "🤝 The series ended in a Draw!"
        messagebox.showinfo("Series Over", final_winner)
        exit_game()
    else:
        # Next round → alternate starter
        set_starting_player()
        restart_game()


# Decide who starts this round
def set_starting_player():
    global current_player, games_played
    if games_played % 2 == 0:
        current_player = "X"
    else:
        current_player = "O"
    status_label.config(text=f"Player {current_player}'s turn")


# Main Window
root = tk.Tk()
root.title("Tic Tac Toe - Series Mode")
root.configure(bg="#2C3E50")
root.resizable(False, False)

# Ask number of games
total_games = simpledialog.askinteger("Game Setup", "How many games will you play?", minvalue=1, maxvalue=20)

current_player = "X"
winner = False
x_score, o_score, draw_score = 0, 0, 0
games_played = 0

# Title
title_label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 28, "bold"), bg="#2C3E50", fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Scoreboard
score_label = tk.Label(root, text="❌ X: 0   ⭕ O: 0   🤝 Draws: 0",
                       font=("Helvetica", 14, "bold"), bg="#2C3E50", fg="white")
score_label.grid(row=1, column=0, columnspan=3, pady=5)

# Status
status_label = tk.Label(root, text=f"Player {current_player}'s turn",
                        font=("Helvetica", 14), bg="#2C3E50", fg="yellow")
status_label.grid(row=2, column=0, columnspan=3, pady=5)

# Buttons (Board)
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Helvetica", 24, "bold"),
                    width=6, height=2, bg="#ECECEC", fg="black",
                    activebackground="#3498DB", activeforeground="white",
                    relief="raised", bd=3,
                    command=lambda i=i: button_click(i))
    btn.grid(row=(i//3)+3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Control Buttons
restart_btn = tk.Button(root, text="🔄 Restart Round", font=("Helvetica", 12, "bold"),
                        bg="#27AE60", fg="white", width=15, command=restart_game)
restart_btn.grid(row=6, column=0, pady=15)

exit_btn = tk.Button(root, text="❌ Exit", font=("Helvetica", 12, "bold"),
                     bg="#E74C3C", fg="white", width=15, command=exit_game)
exit_btn.grid(row=6, column=2, pady=15)

update_scoreboard()
set_starting_player()

root.mainloop()
