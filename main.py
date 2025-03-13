# Using Python 3.12.3
# Dependencies defined in requirements.txt were installed via command "pip install -r requirements.txt"
# Project uses venv via "python3 -m venv venv" -> "source venv/bin/activate"
# .gitignore is used from standard python .gitignore template available on GitHub during project initialization
import pygame

# import pygame_widgets # TBD: widgets can  be used for simpler button creation to improve the GUI of the game, possibly making clickable buttons with nice pictures of RPS 
# (these would then have to be set up within constants.py to link files to correct RPS-"value" and uploaded as part of the project to GitHub as well)

from constants import *
from RPS_game import *


# This function is used to always "return" the user to the initial game screen
def return_to_start(screen):
    screen.fill(BLACK)
    screen.blits(GAME_VARIANT_CHOICE_BLITS)
    pygame.display.flip()

def give_error(screen):
    screen.fill(BLACK)
    screen.blits(ERROR_MSG_RETURN_TO_START)
    waiting = True
    pygame.display.flip()

    pygame.event.clear()
    #print("just cleared event cache")
    #event = pygame.event.wait()
    #print(waiting, "event is", event)  

    while waiting:
        
        #event = pygame.event.wait() #TBD - figure out why the wait event isn't behaving as expected
        #print(waiting, "event is", event) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # currently necessary because we would end in the outer loop, can be taken out once proper looping is implemented
            elif event.type == pygame.KEYDOWN : #or event.type == pygame.KEYUP 
                waiting = False
                return_to_start(screen)
                return

def PC_vs_PC(screen):
    #TBD: it's enough to display the result of the game here, and give the option to rematch or return to "main screen"
    pass

def Human_vs_PC(screen):
    screen.fill(BLACK)
    screen.blits(CHOICE_VARIANT_CHOICE_BLITS)
    waiting = True
    pygame.display.flip()

    pygame.event.clear()
    while waiting:
        
        #event = pygame.event.wait() #TBD - figure out why the wait event isn't behaving as expected
        #print(waiting, "event is", event) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # currently necessary because we would end in the outer loop, can be taken out once proper looping is implemented
            elif event.type == pygame.KEYDOWN : #or event.type == pygame.KEYUP 
                pressed = event.key
                if pressed == pygame.K_1:
                    # TBD: call RPS_game(LIST_OF_RPS[0]) and display result of play
                    pass

                elif pressed == pygame.K_2:
                    # TBD: call RPS_game(LIST_OF_RPS[1]) and display result of play
                    pass

                elif pressed == pygame.K_3:
                    # TBD: call RPS_game(LIST_OF_RPS[2]) and display result of play
                    pass

                #if any other key is pressed, we show and error message to the user and after another keypress of any key return them the starting screen
                else:
                    give_error(screen)
    


def main():
    pygame.init() # optional TBD: init() returns a tuple with number of failed inits, possibly do a check and throw an error if that happens
    
    # setting up some environment variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME) 
    is_running = True

    # Setup game clock in order to control FPS
    # TBD - currently not used    
    game_clock = pygame.time.Clock()
    clock_delta = 0

    # test - ToDelete
    print(RPS_game(LIST_OF_RPS[0]))
    print(RPS_game())


    return_to_start(screen) # we reuse this function also for the "initial" start of the game

    while is_running : # Start of infinite game loop        

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # Checks for the user to close the window and terminates via environment variable is_running
                is_running = False  
                
            if event.type == pygame.KEYDOWN:  # Set up with partial help from: https://www.tutorialspoint.com/pygame/pygame_keyboard_events.htm
                pressed = event.key
                if pressed == pygame.K_ESCAPE or pressed == pygame.K_q:
                    is_running = False
                    
                elif pressed == pygame.K_1:
                    Human_vs_PC(screen) # TBD: 
                    pass

                elif pressed == pygame.K_2:
                    # TBD: PC_vs_PC()
                    pass

                #if any other key is pressed, we show and error message to the user and after another keypress of any key return them the starting screen
                else:
                    give_error(screen)
                        





        clock_delta += game_clock.tick(60)/1000 
        pygame.display.flip() # At the end of the loop refreshes the screen

if __name__ == "__main__": # Ensures that this can be run only directly, not via a call from another module
    main()
