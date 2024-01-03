'''
Author: Code Monkey King
Date: Feb 8, 2024.
Board class.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[1][7] is the square in column 2,
     at the opposite end of the board in row 8.
Squares are stored and manipulated as (x,y) tuples.
x is the column, y is the row.
'''

import numpy as np

class Board():

    # list of all 8 directions on the board, as (x,y) offsets
    #__directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n):
      "Set up initial board configuration."
      self.n = n
      # Create the empty board array.
      self.pieces = [None]*self.n
      for i in range(self.n):
        self.pieces[i] = [0]*self.n

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color, ko):
      """Returns all the legal moves for the given color.
      (1 for white, -1 for black
      """
      moves = set()
      for y in range(self.n):
        for x in range(self.n):
          if self[y][x] == 0 and (x, y) != ko:
            old_board = np.copy(self.pieces)
            self.execute_move((x, y), color, ko)
            liberties = []
            self.count(x, y, color, liberties, [])
            if len(liberties): moves.update({(x, y)})
            self.pieces = np.copy(old_board)
      return list(moves)

    def execute_move(self, move, color, ko):
      """Perform the given move on the board; flips pieces as necessary.
      color gives the color pf the piece to play (1=white,-1=black)
      """
      self[move[1]][move[0]] = color
      return self.captures(-color, ko);
    
    def captures(self, color, ko):
      new_ko = (-1, -1)
      for y in range(self.n):
        for x in range(self.n):
          if self[x][y]==color:
            liberties = []
            block = []
            self.count(x, y, color, liberties, block)
            if len(liberties) == 0:
              if len(block) == 1:
                new_ko = (block[0][1], block[0][0])
              for captured in block:
                self[captured[0]][captured[1]] = 0
            self.restore_board()
      return new_ko

    def count(self, x, y, color, liberties, block):
      if x < 0 or y < 0 or x >= self.n or y >= self.n: return
      if self[x][y] == color:
        block.append((x, y))
        if self[x][y] == 1: self[x][y] = 2
        if self[x][y] == -1: self[x][y] = -2
        self.count(x, y-1, color, liberties, block)
        self.count(x, y+1, color, liberties, block)
        self.count(x-1, y, color, liberties, block)
        self.count(x+1, y, color, liberties, block)
      elif self[x][y] == 0:
        self[x][y] = 3
        liberties.append((x, y))

    def restore_board(self):
      for y in range(self.n):
        for x in range(self.n):
          if self[x][y] == 2: self[x][y] = 1
          if self[x][y] == -2: self[x][y] = -1
          if self[x][y] == 3: self[x][y] = 0

    def evaluate(self, color):
      """Counts the # pieces of the given color
      (1 for white, -1 for black, 0 for empty spaces)"""
      count = 0

      return count

