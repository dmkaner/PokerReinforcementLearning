from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from console_player import ConsolePlayer
from random_player import RandomPlayer
from honest_player import HonestPlayer

config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=20)

config.register_player(name="f1", algorithm=FishPlayer())
config.register_player(name="r1", algorithm=RandomPlayer())
config.register_player(name="h1", algorithm=HonestPlayer())
config.register_player(name="h2", algorithm=HonestPlayer())
config.register_player(name="h3", algorithm=HonestPlayer())
config.register_player(name="h4", algorithm=HonestPlayer())

game_result = start_poker(config, verbose=1)

print(game_result)