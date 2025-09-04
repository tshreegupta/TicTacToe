"""
Author: Tanushree Gupta
Date: 2024-09-04
Email: tshreegupta@gmail.com
Description: Write a program that plays every possible tic-tac-toe game, and then prints the number of 
            possible valid, completed game states.
"""

from typing import List, Set, Tuple


def winner(board: List[str]) -> bool:
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)]             # diagonals
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != "_":
            return True
    return False

def is_full(board: List[str]) -> bool:
    return all(cell != "_" for cell in board)

def dfs(board: List[str], player: str, completed_boards: Set[Tuple[str,...]]):
    next_player = "O" if player == "X" else "X"
    if winner(board):
        completed_boards.add((tuple(board), f"{next_player} Win"))
        return
    elif is_full(board):
        completed_boards.add((tuple(board), "Tie"))
        return
    for i in range(9):
        if board[i] == "_":
            board[i] = player
            dfs(board, next_player, completed_boards)
            board[i] = "_"

def print_stats(completed_boards: Set[Tuple[str,...]]):

    print("="*40)
    print(f"|   Number of completed boards: {len(completed_boards)}")
    print(f"|   Number of X wins: {sum(1 for _,result in completed_boards if result == "X Win")}")
    print(f"|   Number of O wins: {sum(1 for _,result in completed_boards if result == "O Win")}")
    print(f"|   Number of draws: {sum(1 for _,result in completed_boards if result == "Tie")}")
    print("="*40)
    response = input("Print all completed boards:(Y/N)")

    if response.strip().upper() == "Y":
        for board,_ in completed_boards:
            print(board)

def play_tic_tac_toe():
    board = ["_"]*9
    completed_boards: Set[Tuple[str,...]] = set()
    dfs(board, "X", completed_boards)
    print_stats(completed_boards)

if __name__ == '__main__':
    play_tic_tac_toe()