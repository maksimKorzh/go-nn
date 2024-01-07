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
g = GoGame(5)

# nnet players
n1 = NNet(g)
n1.load_checkpoint('./temp', 'temp.pth.tar')
#n1.load_checkpoint('./models', '5x5_1-iteration_100-episodes_10-epochs.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0, 'depth_limit': 100})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x, y: np.argmax(mcts1.getActionProb(x, y, temp=0))

player2 = HumanGoPlayer1(g).play
arena = Arena.Arena(n1p, player2, g, display=GoGame.display)
print(arena.playGames(2, verbose=True))
