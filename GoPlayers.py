import numpy as np


class RandomGoPlayer():
   def __init__(self, game):
     self.game = game

   def play(self, board, ko):
     a = np.random.randint(self.game.getActionSize())
     valids = self.game.getValidMoves(board, 1, ko)
     while valids[a]!=1:
       a = np.random.randint(self.game.getActionSize())
     return a


class HumanGoPlayer1():
    def __init__(self, game):
      self.game = game

    def play(self, board, ko):
      # display(board)
      valid = self.game.getValidMoves(board, 1, ko)
      while True:
        input_move = input()
        input_a = input_move.split(" ")
        if len(input_a) == 2:
          try:
            x,y = [int(i) for i in input_a]
            if ((0 <= x) and \
               (x < self.game.n) and \
               (0 <= y) and \
               (y < self.game.n)) or \
               ((x == self.game.n) and (y == 0)):
              a = self.game.n * x + y if x != -1 else self.game.n ** 2
              if valid[a]: break
          except ValueError:
            # Input needs to be an integer
            'Invalid integer'
        print('Invalid move')
      return a

class HumanGoPlayer2():
    def __init__(self, game):
      self.game = game

    def play(self, board, ko):
      # display(board)
      valid = self.game.getValidMoves(board, -1, ko)
      while True:
        input_move = input()
        input_a = input_move.split(" ")
        if len(input_a) == 2:
          try:
            x,y = [int(i) for i in input_a]
            if ((0 <= x) and \
               (x < self.game.n) and \
               (0 <= y) and \
               (y < self.game.n)) or \
               ((x == self.game.n) and (y == 0)):
              a = self.game.n * x + y if x != -1 else self.game.n ** 2
              if valid[a]: break
          except ValueError:
            # Input needs to be an integer
            'Invalid integer'
        print('Invalid move')
      return a
