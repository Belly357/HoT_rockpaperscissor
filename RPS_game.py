import random
from constants import * # TBD - adjust import to import only the required constants, not all

# We use this function to "play" the RPS game, in takes an optional argument so we can use it 
# for both cases when Player plays against PC and PC vs PC. 
# Returns the "played" values of both sides and an integer to mark if the first 
# player (the human or the first PC) was a winner, loser, or it was a tie (0,1 or 8 respectively) 
# Note: Arguably, the last game_result[2] could be text instead of an integer 
def RPS_game(player_choice = None):
    game_result = [None, None, None]

    # if the player has chosen an RPS by themselves, set it as first of game_result, otherwise choose it
    if player_choice == None:
        game_result[0] = random.choice(LIST_OF_RPS)
    else:
        game_result[0] = player_choice

    # TBD: make a check/throw an exception in case the player_choice isn't a valid value from LIST_OF_RPS

    # the second choice is always randomly chosen by
    game_result[1] = random.choice(LIST_OF_RPS)

    # Here we define the winning condition of player 1, be it Human or PC player. 
    # Should the game be enhanced, e.g. new values in LIST_OF_RPS, these rules have to be adjusted as well. 
    # A point or TBD to make: Maybe the rules of winning, i.e. which LIST_OF_RPS value beats which could be 
    # defined rather in constants so adjustment to the game can be made only in one place?

    # A draw in case both are the same
    if game_result[0] == game_result[1]:
        game_result[2] = 8

    # defines wins for player 1:
    if \
    (game_result[0] == LIST_OF_RPS[0] and game_result[1] == LIST_OF_RPS[2]) or \
    (game_result[0] == LIST_OF_RPS[1] and game_result[1] == LIST_OF_RPS[0]) or \
    (game_result[0] == LIST_OF_RPS[2] and game_result[1] == LIST_OF_RPS[1]):
        game_result[2] = 0

    # defines loses for player 1:
    if \
    (game_result[0] == LIST_OF_RPS[2] and game_result[1] == LIST_OF_RPS[0]) or \
    (game_result[0] == LIST_OF_RPS[0] and game_result[1] == LIST_OF_RPS[1]) or \
    (game_result[0] == LIST_OF_RPS[1] and game_result[1] == LIST_OF_RPS[2]):
        game_result[2] = 1    
    
    return game_result