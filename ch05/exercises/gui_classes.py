class Player:
	def __init__(character):
          character.player_num = 1
          character.distance = 0 # player always has travelled 0 distance at the start
          character.coins = 0 # players always start with 0 coins collected
          character.is_moving = False # player always starts still

class MysteryBlock:
	def __init__(block):
          block.block_num = 1
          block.blink = 0 # mystery block blinks 0 times at the start of the game
          block.inscreen = True # mystery block is in screen at the start of the game
          block.lighton = False # mystery block isn't lighted up at the start of the game
    
class Mushroom:
	def __init__(mushroom):
          mushroom.mushroom_num = 1
          mushroom.collected = False # mushroom is not collected by player at the start of the game
          mushroom.color = "red" # mushroom is red in color
          mushroom.inscreen = True # mushroom is in screen at the start of the game