# gui.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from game_logic import TicTacToeGame

class TicTacToeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.game = TicTacToeGame()  # Initialize game logic
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 100, 400, 400)  # Set window geometry
        self.setWindowTitle('Tic Tac Toe')     # Set window title
        
        # Create layout for game board
        self.board_layout = QVBoxLayout()
        self.buttons = []  # List to store button references
        
        for i in range(3):
            row_layout = QHBoxLayout()
            for j in range(3):
                button = QPushButton('')
                button.setStyleSheet('''
                    QPushButton {
                        border: 2px solid #000;
                        font-size: 24px;
                        width: 80px;
                        height: 80px;
                    }
                ''')
                button.clicked.connect(lambda state, x=i, y=j: self.place_token(x, y))
                row_layout.addWidget(button)
                self.buttons.append(button)
            self.board_layout.addLayout(row_layout)
        
        self.setLayout(self.board_layout)
        self.show()

    def place_token(self, x, y):
        self.game.place_token(x, y)  # Call the place_token method from game logic
        button = self.buttons[x * 3 + y]
        button.setText(self.game.get_board()[x][y])  # Update button text with token

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToeGUI()
    sys.exit(app.exec_())