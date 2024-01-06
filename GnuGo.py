#
# GnuGo subprocess to keep track
#    of current board state
#

import pexpect
import numpy as np

class GnuGo():
  def __init__(self, size, komi):
    # Store board size
    self.size = size

    # Start engine subprocess
    self.gnugo = pexpect.spawnu('gnugo --mode gtp')

    # Init commands
    init_commands = [
      'name',
      'version',
      'protocol_version',
      'komi ' + str(komi),
      'boardsize ' + str(size),
      'clear_board'
    ]

    # Init engine
    for command in init_commands:
      self.gnugo.sendline(command)
      self.gnugo.expect('= (.*)', timeout = -1)
 
  def printBoardState(self):
    self.gnugo.sendline('showboard')
    self.gnugo.expect('= (.*)', timeout = -1)
    brd = self.gnugo.after.strip()
    brd = brd.replace('WHITE (O) has captured ', '0: ')
    brd = brd.replace('BLACK (X) has captured ', 'X: ')
    brd = brd.replace('stones', 'caps')
    print(brd)

  def getBoardState(self):
    self.gnugo.sendline('showboard')
    self.gnugo.expect('= (.*)', timeout = -1)
    brdStr = self.gnugo.after.strip().split('=')[-1][1:-1]
    brdStr = [row.replace(' ', '')[1: self.size+1] for row in brdStr.split('\n')[2:-1]]
    brdArr = zeros_array = np.zeros((self.size, self.size)).astype(int)
    for y in range(len(brdStr)):
      line = brdStr[y]
      for x in range(len(line)):
        if line[x] == 'X': brdArr[y][x] = int(1)
        if line[x] == 'O': brdArr[y][x] = int(-1)
    return brdArr

  def getAllLegal(self, color):
    self.gnugo.sendline('all_legal ' + 'B' if color == 1 else 'W')
    self.gnugo.expect('= (.*)', timeout = -1)
    moves = self.gnugo.after.strip().split()[1:]
    for i in range(len(moves)):
      moves[i] = ('ABCDEFGHJKLMNOPQRST'.index(moves[i][0]), int(moves[i][1]))
    return set(moves)

  def play(self, move, color):
    moveColor = 'B' if color == 1 else 'W'
    moveCoord = ' ' + 'ABCDEFGHJKLMNOPQRST'[move[0]] + str(self.size - move[1])
    moveCmd = 'play ' + moveColor + moveCoord
    self.gnugo.sendline(moveCmd)
    self.gnugo.expect('= (.*)', timeout = -1)

def test():
  gnugo = GnuGo(5, 5.5)
  pieces = gnugo.getBoardState()
  gnugo.getAllLegal(1)
  print(pieces)
#test()
