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
    brd = self.gnugo.after.strip().split('=')[-1]
    brd = brd.replace('WHITE (O) has captured ', '0: ')
    brd = brd.replace('BLACK (X) has captured ', 'X: ')
    brd = brd.replace('stones', 'caps')
    print(brd)

  def getBoardState(self):
    self.gnugo.sendline('showboard')
    self.gnugo.flush()
    self.gnugo.expect('= (.*)', timeout = -1)
    brdStr = self.gnugo.after.strip().split('=')[-1][1:-1]
    brdStr = [row.replace(' ', '')[1: self.size+1] for row in brdStr.split('\n')[2:-1]]
    if len(brdStr) < self.size: self.getBoardState();
    brdArr = zeros_array = np.zeros((self.size, self.size)).astype(int)
    for y in range(len(brdStr)):
      line = brdStr[y]
      for x in range(len(line)):
        if line[x] == 'X': brdArr[y][x] = int(1)
        if line[x] == 'O': brdArr[y][x] = int(-1)
    return brdArr

  def getAllLegal(self, color):
    cmd = 'all_legal ' + ('B' if color == 1 else 'W')
    self.gnugo.sendline(cmd)
    self.gnugo.expect('= (.*)', timeout = -1)
    moves = self.gnugo.after.strip().split()[1:]
    for i in range(len(moves)):
      moves[i] = ('ABCDEFGHJKLMNOPQRST'.index(moves[i][0]), self.size-int(moves[i][1]))
    return set(moves)

  def play(self, move, color):
    moveColor = 'B' if color == 1 else 'W'
    moveCoord = ' ' + 'ABCDEFGHJKLMNOPQRST'[move[0]] + str(self.size - move[1])
    moveCmd = 'play ' + moveColor + moveCoord
    self.gnugo.sendline(moveCmd)
    self.gnugo.expect('= (.*)', timeout = -1)

  def estimateScore(self):
    self.gnugo.sendline('estimate_score')
    self.gnugo.expect('= (.*)', timeout = -1)
    print('GnuGo.estimateScore:', self.gnugo.after)
    try: return (1 if self.gnugo.after[2] == 'B' else -1)
    except: self.estimateScore()

  def generateMove(self, color):
    self.gnugo.sendline('genmove ' + ('B' if color == 1 else 'W'))
    self.gnugo.expect('= (.*)', timeout = -1)
    return (0 if 'PASS' in self.gnugo.after else 1)
    
def test():
  gnugo = GnuGo(5, 5.5)
  pieces = gnugo.getBoardState()
  moves = gnugo.getAllLegal(1)
  gnugo.printBoardState()
  print(moves)
  gnugo.estimateScore()
#test()
