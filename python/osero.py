import tkinter as tk
from tkinter import messagebox

class ReversiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reversi")
        self.board = [["." for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = "W"
        self.board[3][4] = self.board[4][3] = "B"
        self.current_player = "B"
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()
        self.update_board()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                button = tk.Button(self.root, width=4, height=2, command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        if self.is_valid_move(self.board, row, col, self.current_player):
            self.make_move(self.board, row, col, self.current_player)
            self.current_player = "W" if self.current_player == "B" else "B"
            self.update_board()
            if not self.has_valid_moves(self.board, self.current_player):
                self.current_player = "W" if self.current_player == "B" else "B"
                if not self.has_valid_moves(self.board, self.current_player):
                    self.end_game()

    def update_board(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == "B":
                    self.buttons[row][col].config(bg="black", state=tk.DISABLED)
                elif self.board[row][col] == "W":
                    self.buttons[row][col].config(bg="white", state=tk.DISABLED)
                else:
                    self.buttons[row][col].config(bg="green", state=tk.NORMAL)

    def is_valid_move(self, board, row, col, player):
        if board[row][col] != ".":
            return False
        opponent = "W" if player == "B" else "B"
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                while 0 <= r < 8 and 0 <= c < 8:
                    r += dr
                    c += dc
                    if r < 0 or r >= 8 or c < 0 or c >= 8:
                        break
                    if board[r][c] == ".":
                        break
                    if board[r][c] == player:
                        return True
        return False

    def make_move(self, board, row, col, player):
        board[row][col] = player
        opponent = "W" if player == "B" else "B"
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                pieces_to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                for rr, cc in pieces_to_flip:
                    board[rr][cc] = player

    def has_valid_moves(self, board, player):
        return any(self.is_valid_move(board, row, col, player) for row in range(8) for col in range(8))

    def end_game(self):
        black_count, white_count = self.count_pieces(self.board)
        if black_count > white_count:
            winner = "Black wins!"
        elif white_count > black_count:
            winner = "White wins!"
        else:
            winner = "It's a tie!"
        messagebox.showinfo("Game Over", f"Game over. Black: {black_count}, White: {white_count}\n{winner}")
        self.root.quit()

    def count_pieces(self, board):
        black_count = sum(row.count("B") for row in board)
        white_count = sum(row.count("W") for row in board)
        return black_count, white_count

if __name__ == "__main__":
    root = tk.Tk()
    game = ReversiGame(root)
    root.mainloop()
