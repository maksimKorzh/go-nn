import Arena
from MCTS import MCTS
from GoGame import GoGame
from GoPlayers import *
from NNet import NNetWrapper as NNet


import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

#mini_othello = False  # Play in 6x6 instead of the normal 8x8.
human_vs_cpu = True

g = GoGame(5)

# Old net
n1 = NNet(g)
n1.load_checkpoint('./temp', 'last.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x, y: np.argmax(mcts1.getActionProb(x, y, temp=0))

# New net
n2 = NNet(g)
n2.load_checkpoint('./models', '5x5_1-iteration_100-episodes_10-epochs.pth.tar')
args2 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts2 = MCTS(g, n2, args2)
n2p = lambda x, y: np.argmax(mcts2.getActionProb(x, y, temp=0))
#n2p = HumanGoPlayer1(g).play

print('PLAYING AGAINST PREVIOUS VERSION')
arena = Arena.Arena(n1p, n2p, g, display=GoGame.display)
pwins, nwins, draws = arena.playGames(10, verbose=True)
print("Previous wins:", pwins, "New wins:", nwins, "Draws:", draws)