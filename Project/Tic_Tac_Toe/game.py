import tkinter as tk
from tkinter import messagebox

def check_winner():
    global game_over
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    # Check for a winner
    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for index in combo:
                buttons[index].config(bg="green")
            game_over = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            return
    
    # Check for a draw (when all buttons are filled and no winner)
    if all(button["text"] != "" for button in buttons):
        game_over = True
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        return

def button_click(index):
    if buttons[index]["text"] == "" and not game_over:
        buttons[index]["text"] = current_player
        check_winner()
        if not game_over:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game state
current_player = 'X'
game_over = False

# Create a label to display the current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Create the buttons for the Tic-Tac-Toe grid
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Arrange the buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Start the Tkinter event loop
root.mainloop()

