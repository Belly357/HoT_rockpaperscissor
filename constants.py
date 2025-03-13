# Maybe not really a standard for a constants file, but I've decided to import pygame also here in order to be able to Setup textation (and later on possibly button) as constants
# The reasoning is, that textation like game rules can be adjusted via this constants file and when enhancing the game, would not require changes within the main.py file. Also the textation, Button colors etc. should be a constant
import pygame
pygame.font.init() # in order to use font, we have to initialize them, but there's no need to init the whole pygame, i.e. pygame.init() 

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

GAME_NAME = "HoT Excercise - Rock paper scissor"

#Color references so that shades can be adjusted via changes the constants if needed
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 223)
RED = (160, 0, 0)

LIST_OF_RPS = ["Rock", "Paper", "Scissor"]
NUMBER_OF_RPS = len(LIST_OF_RPS) # an agregated constant, can be used in future to expand upon the game, e.g. Rock-Paper-Scissor-Snake-Spock

#Dictonary pairing of RPS value to text color for text version of the game:
RPS_COLORS = {LIST_OF_RPS[0]: BLUE, LIST_OF_RPS[1]: GREEN, LIST_OF_RPS[2]: RED}


#Game textation - currently valid for the text version of the game:
FONT = pygame.font.Font('freesansbold.ttf', 32)

#These are done manually for now, but a multi-line creator function would be useful for the future, where the RPS game is enhanced with new values. One still would have to "manually" calculate the position of each line, 
# as pygame can only render one line and ignored \n 
# idea for the function taken from: https://www.reddit.com/r/pygame/comments/ezohr9/how_do_i_add_multiline_text_in_pygame/ and https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
RULES_TEXT_1 = "Please press a corresponding key to choose game mode:"  
RULES_TEXT_2 = "1 -> I want to play against PC"
RULES_TEXT_3 = "2 -> I want to see two PCs duke it out"
RULES_TEXT_4 = "Q -> quit the program"

GAME_RULES_1 = FONT.render(RULES_TEXT_1, True, WHITE, BLACK)
GAME_RULES_RECT_1 = GAME_RULES_1.get_rect()
GAME_RULES_RECT_1.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) - 34)

GAME_RULES_2 = FONT.render(RULES_TEXT_2, True, WHITE, BLACK)
GAME_RULES_RECT_2 = GAME_RULES_2.get_rect()
GAME_RULES_RECT_2.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ))

GAME_RULES_3 = FONT.render(RULES_TEXT_3, True, WHITE, BLACK)
GAME_RULES_RECT_3 = GAME_RULES_3.get_rect()
GAME_RULES_RECT_3.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) + 34)

GAME_RULES_4 = FONT.render(RULES_TEXT_4, True, WHITE, BLACK)
GAME_RULES_RECT_4 = GAME_RULES_4.get_rect()
GAME_RULES_RECT_4.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) + 102)

# We will be rendering the 4 above lines always together, thus we create an aggregate Constant to pass to the blits renderer
GAME_VARIANT_CHOICE_BLITS = ((GAME_RULES_1, GAME_RULES_RECT_1), (GAME_RULES_2, GAME_RULES_RECT_2), (GAME_RULES_3, GAME_RULES_RECT_3), (GAME_RULES_4, GAME_RULES_RECT_4))

# We repeat the same to show the player his choice of RPS, once again done here manually for now, but should be change to a function that build the "multiline text list of touples" to pass to the blits renderer
CHOICE_TEXT_1 = "Please press a corresponding key to choose which RPS you'll play"  
CHOICE_TEXT_2 = "1 -> I want to play " + LIST_OF_RPS[0] # we build the text based on our existing LIST_OF_RPS constant, so we can make translation of modifications to the game easier 
CHOICE_TEXT_3 = "2 -> I want to play " + LIST_OF_RPS[1]
CHOICE_TEXT_4 = "3 -> I want to play " + LIST_OF_RPS[2]

CHOICE_RULES_1 = FONT.render(CHOICE_TEXT_1, True, WHITE, BLACK)
CHOICE_RULES_RECT_1 = CHOICE_RULES_1.get_rect()
CHOICE_RULES_RECT_1.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) - 34)

CHOICE_RULES_2 = FONT.render(CHOICE_TEXT_2, True, RPS_COLORS[LIST_OF_RPS[0]], BLACK)
CHOICE_RULES_RECT_2 = CHOICE_RULES_2.get_rect()
CHOICE_RULES_RECT_2.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ))

CHOICE_RULES_3 = FONT.render(CHOICE_TEXT_3, True, RPS_COLORS[LIST_OF_RPS[1]], BLACK)
CHOICE_RULES_RECT_3 = CHOICE_RULES_3.get_rect()
CHOICE_RULES_RECT_3.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) + 34)

CHOICE_RULES_4 = FONT.render(CHOICE_TEXT_4, True, RPS_COLORS[LIST_OF_RPS[2]], BLACK)
CHOICE_RULES_RECT_4 = CHOICE_RULES_4.get_rect()
CHOICE_RULES_RECT_4.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) + 68)

# We will be rendering the 4 above lines always together, thus we create an aggregate Constant to pass to the blits renderer
CHOICE_VARIANT_CHOICE_BLITS = ((CHOICE_RULES_1, CHOICE_RULES_RECT_1), (CHOICE_RULES_2, CHOICE_RULES_RECT_2), (CHOICE_RULES_3, CHOICE_RULES_RECT_3), (CHOICE_RULES_4, CHOICE_RULES_RECT_4))

# Here we make an error message that will be used in case the user presses any unexpected key
ERROR_MSG_TEXT_1 = "The key pressed is an unknown input, please choose only valid option!"
ERROR_MSG_TEXT_2 = "Press any key to return to start."

ERR_MSG_R_T_S_1 = FONT.render(ERROR_MSG_TEXT_1, True, WHITE, BLACK)
ERR_MSG_R_T_S_RECT_1 = ERR_MSG_R_T_S_1.get_rect()
ERR_MSG_R_T_S_RECT_1.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ) - 34)

ERR_MSG_R_T_S_2 = FONT.render(ERROR_MSG_TEXT_2, True, WHITE, BLACK)
ERR_MSG_R_T_S_RECT_2 = ERR_MSG_R_T_S_2.get_rect()
ERR_MSG_R_T_S_RECT_2.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 ))

ERROR_MSG_RETURN_TO_START = ((ERR_MSG_R_T_S_1, ERR_MSG_R_T_S_RECT_1), (ERR_MSG_R_T_S_2, ERR_MSG_R_T_S_RECT_2))