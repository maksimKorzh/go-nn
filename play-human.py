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

n1p = HumanGoPlayer1(g).play
n2p = HumanGoPlayer2(g).play
arena = Arena.Arena(n1p, n2p, g, display=GoGame.display)
print(arena.playGames(2, verbose=True))
