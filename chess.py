#defining the chess board where the game will be held

class ChessGame:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
            ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
            [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
            ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ]

    def move(self, x1, y1, x2, y2):
        piece = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.board[y2][x2] = piece

    def display(self):
        for row in self.board:
            print(' '.join(row))

game = ChessGame()
game.display()

class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, x1, y1, x2, y2, board):
        return False

class Pawn(Piece):
    def is_valid_move(self, x1, y1, x2, y2, board):
        piece = board[y1][x1]
        if self.color == 'white':
            if y2 == y1 - 1 and x1 == x2 and board[y2][x2] == ' ':
                return True
            elif y2 == y1 - 1 and abs(x2 - x1) == 1 and board[y2][x2] != ' ' and board[y2][x2].islower():
                return True
            elif y1 == 6 and y2 == 4 and x1 == x2 and board[5][x1] == ' ' and board[4][x1] == ' ':
                return True
        elif self.color == 'black':
            if y2 == y1 + 1 and x1 == x2 and board[y2][x2] == ' ':
                return True
            elif y2 == y1 + 1 and abs(x2 - x1) == 1 and board[y2][x2] != ' ' and board[y2][x2].isupper():
                return True
            elif y1 == 1 and y2 == 3 and x1 == x2 and board[2][x1] == ' ' and board[3][x1] == ' ':
                return True
        return False

class Knight(Piece):
    def is_valid_move(self, x1, y1, x2, y2, board):
        piece = board[y1][x1]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx == 2 and dy == 1 or dx == 1 and dy == 2:
            if board[y2][x2] == ' ' or piece.islower() != board[y2][x2].islower():
                return True
        return False

class Bishop(Piece):
    def is_valid_move(self, x1, y1, x2, y2, board):
        piece = board[y1][x1]
        if abs(x2 - x1) == abs(y2 - y1):
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            x, y = x1 + dx, y1 + dy
            while x != x2 and y != y2:
                if board[y][x] != ' ':
                    return False
                x += dx
                y += dy
            if board[y2][x2] == ' ' or piece.islower() != board[y2][x2].islower():
                return True
        return False

class Rook(Piece):
    def is_valid_move(self, x1, y1, x2, y2, board):
        piece = board[y1][x1]
        if x1 == x2:
            dx = 0
            dy = 1 if y2 > y1 else -1
        elif y1 == y2:
            dx = 1 if x2 > x1 else -1
            dy = 0
        else:
            return False
        x, y = x1 + dx
		
		from random import choice

class Chess:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ]
        self.turn = 'white'
        self.game_over = False

    def display_board(self):
        print('  a b c d e f g h')
        print('  ---------------')
        for i in range(8):
            row = str(8 - i) + '|'
            for j in range(8):
                row += self.board[i][j] + '|'
            print(row)
            print('  ---------------')
        print('  a b c d e f g h')

    def is_valid_move(self, x1, y1, x2, y2):
        piece = self.board[y1][x1]
        if piece == ' ' or (self.turn == 'white' and piece.islower()) or (self.turn == 'black' and piece.isupper()):
            return False
        if x1 == x2 and y1 == y2:
            return False
        return Piece.create(piece, self.turn).is_valid_move(x1, y1, x2, y2, self.board)

    def move(self, x1, y1, x2, y2):
        if not self.is_valid_move(x1, y1, x2, y2):
            return False
        piece = self.board[y1][x1]
        self.board[y1][x1] = ' '
        self.board[y2][x2] = piece
        self.turn = 'white' if self.turn == 'black' else 'black'
        return True

    def play(self):
        while not self.game_over:
            self.display_board()
            while True:
                move = input(f'{self.turn.capitalize()}\'s move (e.g. e2 e4): ').strip()
                if len(move) != 5 or move[2] != ' ':
                    print('Invalid move')
                    continue
                x1, y1 = ord(move[0]) - ord('a'), 8 - int(move[1])
                x2, y2 = ord(move[3]) - ord('a'), 8 - int(move[4])
                if not self.move(x1, y1, x2, y2):
                    print('Invalid move')
                    continue
                break
            if self.is_checkmate():
                print(f'{self.turn.capitalize()} wins by checkmate!')
                self.game_over = True
            elif self.is_stalemate():
                print('Stalemate!')
                self.game_over = True
            elif self.is_draw():
                print('Draw!')
                self.game_over = True
            else:
                print(f'{self.turn.capitalize()} to move')
                x1, y



