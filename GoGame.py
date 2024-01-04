from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from GoLogic import Board
import numpy as np

class GoGame(Game):
    square_content = {
        -1: "0",
        +0: ".",
        +1: "X"
    }

    @staticmethod
    def getSquarePiece(piece):
      return GoGame.square_content[piece]

    def __init__(self, n):
      self.n = n

    def getInitBoard(self):
      # return initial board (numpy board)
      b = Board(self.n)
      return np.array(b.pieces)

    def getBoardSize(self):
      # (a,b) tuple
      return (self.n, self.n)

    def getActionSize(self):
      # return number of actions
      return self.n*self.n + 1 # TODO: +1 ???

    def getNextState(self, board, player, action, ko):
      # if player takes action on board, return next (board,player)
      # action must be a valid move
      if action == self.n*self.n: # TODO: pass? not valid?
        return (board, -player)
      b = Board(self.n)
      b.pieces = np.copy(board)
      move = (int(action/self.n), action%self.n)
      ko = b.execute_move(move, player, ko)
      return (b.pieces, -player, ko)

    def getValidMoves(self, board, player, ko):
      # return a fixed size binary vector
      valids = [0]*self.getActionSize()
      b = Board(self.n)
      b.pieces = np.copy(board)
      legalMoves =  b.get_legal_moves(player, ko)
      if len(legalMoves)==0:
        valids[-1]=1
        return np.array(valids)
      for x, y in legalMoves:
        valids[self.n*x+y]=1
      return np.array(valids)

    def getGameEnded(self, board, player):
      # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
      b = Board(self.n)
      b.pieces = np.copy(board)
      finalScore = b.score_game()
      if finalScore[0]: return 0
      elif finalScore[1] == self.n ** 2 - 1: return 0
      else: return 1 if finalScore[1] > finalScore[-1] else -1

    def getCanonicalForm(self, board, player):
      # return state if player==1, else return -state if player==-1
      return player*board

    def getSymmetries(self, board, pi):
      # mirror, rotational
      assert(len(pi) == self.n**2+1)  # 1 for pass
      pi_board = np.reshape(pi[:-1], (self.n, self.n))
      l = []
      for i in range(1, 5):
        for j in [True, False]:
          newB = np.rot90(board, i)
          newPi = np.rot90(pi_board, i)
          if j:
            newB = np.fliplr(newB)
            newPi = np.fliplr(newPi)
          l += [(newB, list(newPi.ravel()) + [pi[-1]])]
      return l

    def stringRepresentation(self, board):
      return board.tostring()

    def stringRepresentationReadable(self, board):
      board_s = "".join(self.square_content[square] for row in board for square in row)
      return board_s

    @staticmethod
    def display(board):
      n = board.shape[0]
      print('\n   ', end='')
      for y in range(n): print(y, end=' ')
      print('')
      for y in range(n):
        print(y, ' ', end='')    # print the row #
        for x in range(n):
          piece = board[y][x]    # get the piece to print
          print(GoGame.square_content[piece], end=' ')
        print('')
      print('')

def test():
  game = GoGame(5)
  #board = game.getInitBoard()
  board = np.array([
    [0, 0, -1, 1, 0],
    [0, 0, -1, 1, 0],
    [0, 0, -1, 1, 0],
    [-1, -1, -1, 1, 1],
    [0, 0, -1, 1, 0],
  ])
  player = 1
  ko = (-1, -1)
  game.display(board)
  print(game.getGameEnded(board, player))
  game.display(board)
#test()
