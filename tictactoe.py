import tkinter as tk
from tkinter import messagebox

# Function to check winner
def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="red")
            buttons[combo[2]].config(bg="yellow")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return
    
    # Check for draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        winner = True


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
    label.config(text=f"Player {current_player}'s turn")


# Restart the game
def restart_game():
    global current_player, winner
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")


# Main Window
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
winner = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 15))
label.grid(row=0, column=0, columnspan=3)

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

restart_btn = tk.Button(root, text="Restart", font=("normal", 12), command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3)

root.mainloop()
