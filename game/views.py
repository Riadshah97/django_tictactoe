from django.shortcuts import render, redirect
from .models import TicTacToeGame

# Create your views here.
def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != '-':
            return board[condition[0]]
    return None

def is_draw(board):
    return '-' not in board

def play_game(request):
    if request.method == 'POST':
        board = list(request.POST.get('board'))
        move = int(request.POST.get('move'))
        player = request.POST.get('player')
        
        # Make the move if the cell is empty
        if board[move] == '-':
            board[move] = player
        
        winner = check_winner(board)
        if winner:
            message = f"{winner} wins!"
        elif is_draw(board):
            message = "It's a draw!"
        else:
            message = f"Next turn: {'O' if player == 'X' else 'X'}"

        context = {
            'board': ''.join(board),
            'player': 'O' if player == 'X' else 'X',
            'message': message,
        }
        return render(request, 'game/board.html', context)

    # Initial state
    return render(request, 'game/board.html', {'board': '---------', 'player': 'X'})