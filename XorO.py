import copy
import enum
from random import choice



class Player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return Player.x if self == Player.o else Player.o

class Choice:
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth

    def __str__(self):
        return f"{str(self.move)}: {str(self.value)}"

class AbBot:
    def __init__(self, player):
        self.player = player

    
    
    def alpha_beta_search(self, board, is_max, current_player, depth, alpha, beta):
        winner = board.has_winner()
        if winner == self.player:
            return Choice(None, 10 - depth, depth)
        elif winner == self.player.other:
            return Choice(None, -10 + depth, depth)
        elif len(board.moves) == 9:
            return Choice(None, 0, depth)

        candidates = board.get_legal_moves()
        max_choice = None
        min_choice = None

        for i in range(len(candidates)):
            row, col = candidates[i]
            new_board = copy.deepcopy(board)
            new_board.make_move(row, col, current_player)
            result = self.alpha_beta_search(
                new_board, not is_max, current_player.other, depth + 1, alpha, beta
            )

            if is_max:
                alpha = max(result.value, alpha)
                if alpha >= beta:
                    return result
            else:
                beta = min(result.value, beta)
                if alpha >= beta:
                    return result

            result.move = (row, col)

            if is_max and (max_choice is None or result.value > max_choice.value):
                max_choice = result
            elif not is_max and (min_choice is None or result.value < min_choice.value):
                min_choice = result

        return max_choice if is_max else min_choice

    def select_move(self, board):
        choice = self.alpha_beta_search(board, True, self.player, 0, -100, 100)
        return choice.move

class Board:
    def __init__(self):
        self.dimension = 3
        self.grid = [[None for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.moves = []

    def print(self):
        print()
        for row in range(self.dimension):
            line = [MARKER_TO_CHAR[self.grid[row][col]] for col in range(self.dimension)]
            print("%s" % "".join(line))

    def has_winner(self):
        if len(self.moves) < 5:
            return None

        for row in range(self.dimension):
            unique_rows = set(self.grid[row])
            if len(unique_rows) == 1:
                value = unique_rows.pop()
                if value is not None:
                    return value

        for col in range(self.dimension):
            unique_cols = {self.grid[row][col] for row in range(self.dimension)}
            if len(unique_cols) == 1:
                value = unique_cols.pop()
                if value is not None:
                    return value

        backwards_diag = {self.grid[i][i] for i in range(self.dimension)}
        if len(backwards_diag) == 1:
            value = backwards_diag.pop()
            if value is not None:
                return value

        forwards_diag = {self.grid[i][self.dimension - 1 - i] for i in range(self.dimension)}
        if len(forwards_diag) == 1:
            value = forwards_diag.pop()
            if value is not None:
                return value
        return None

    def make_move(self, row, col, player):
        if self.is_space_empty(row, col):
            self.grid[row][col] = player
            self.moves.append((row, col))
        else:
            raise Exception("Attempting to move onto already occupied space")

    def last_move(self):
        return self.moves[-1]

    def is_space_empty(self, row, col):
        return self.grid[row][col] is None

    def get_legal_moves(self):
        choices = []
        for row in range(self.dimension):
            choices.extend([(row, col) for col in range(self.dimension) if self.is_space_empty(row, col)])
        return choices

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}
        dp = Board()
        dp.grid = [row[:] for row in self.grid]
        dp.moves = self.moves[:]
        return dp


    # остальные методы доски...

MARKER_TO_CHAR = {
    None: " .. ",
    Player.x: " x ",
    Player.o: " o ",
}
