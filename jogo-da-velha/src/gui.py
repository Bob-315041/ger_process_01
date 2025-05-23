from tkinter import Tk, Button, messagebox, StringVar, Frame
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.master.geometry("400x400")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()
        
    def create_widgets(self):
        frame = Frame(self.master)
        frame.pack()

        for i in range(9):
            button = Button(frame, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = self.current_player
            self.buttons[move].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            else:
                self.current_player = "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()