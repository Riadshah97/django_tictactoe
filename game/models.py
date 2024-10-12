from django.db import models

# Create your models here.
class TicTacToeGame(models.Model):
    board = models.CharField(max_length=9, default="---------")  # 9 cells of the board (e.g., 'XOX--O---')
    current_turn = models.CharField(max_length=1, choices=[('X', 'X'), ('O', 'O')], default='X')
    winner = models.CharField(max_length=1, choices=[('X', 'X'), ('O', 'O'), ('D', 'Draw')], null=True, blank=True)  # For storing winner
    created_at = models.DateTimeField(auto_now_add=True)