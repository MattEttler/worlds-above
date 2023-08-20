from enum import Enum

GameState = Enum('GameState', ['BOOTING', 'RUNNING', 'OVER', 'QUIT'])
game_state = GameState.BOOTING
