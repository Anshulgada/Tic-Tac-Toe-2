from collections import deque

class TicTacToeGame:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
        ]
        self.game_over = False
        self.winner = None
        self.initial_placement_complete = False  # Flag to track initial placement phase
        self.tokens_queue = deque()  # Queue to store tokens in FIFO order

    def place_token(self, x, y):
        if not self.game_over and self.initial_placement_complete:
            self.move_token(x, y)
        elif not self.game_over:
            self.place_initial_token(x, y)

    def place_initial_token(self, x, y):
        if self.board[x][y] == '':
            self.board[x][y] = self.current_player
            self.tokens_queue.append((x, y))  # Add token to queue
            self.check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if len(self.tokens_queue) == 6:  # Check if all tokens are placed
                self.initial_placement_complete = True
                self.current_player = 'X'  # Set current player for moving phase


    def move_token(self, x, y):
        if (x, y) in self.tokens_queue:  # Check if the selected token is in the queue
            token_x, token_y = self.tokens_queue.popleft()  # Remove token from queue
            if self.board[x][y] == '':  # Check if the target position is empty
                self.board[x][y] = self.current_player  # Move the token to the target position
                self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch players
                self.check_winner()  # Check for a winner after the move
                if len(self.tokens_queue) == 0:  # Check if all tokens have been moved
                    self.game_over = True  # If all tokens are moved, end the game
            else:
                self.tokens_queue.appendleft((token_x, token_y))  # Return the token to the queue if the target position is not empty

    def check_winner(self):
        for combo in self.winning_combinations:
            symbols = [self.board[x][y] for x, y in combo]
            if symbols == ['X', 'X', 'X']:
                self.winner = 'X'
                self.game_over = True
            elif symbols == ['O', 'O', 'O']:
                self.winner = 'O'
                self.game_over = True

    def get_board(self):
        return self.board
