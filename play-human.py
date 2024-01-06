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

player1 = HumanGoPlayer1(g).play
player2 = HumanGoPlayer2(g).play
arena = Arena.Arena(player1, player2, g, display=GoGame.display)
print(arena.playGames(2, verbose=True))
