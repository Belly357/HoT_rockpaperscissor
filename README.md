# HoT_rockpaperscissor
Test project for HoT - a simple game of rock paper scissor playable as human vs PC or PC vs PC

Build upon helpful experience from https://github.com/Belly357/BOOTDEV_asteroids , a coding course project done via boot.dev course platform.

See requirements.txt for dependencies to run the project, following are rough steps to run this project:

1, Have python3 installed
2, Have pygame installed
3, Via git / github or other preferred method create a new repo and pull the whole main branch, e.g. run in your CLI " gh repo clone Belly357/HoT_rockpaperscissor "
4, Run main.py, e.g. in your CLI run " python3 main.py "

//////////////////////
Notes and comments for the HoT Excercise reviewers
//////////////////////

Following are comments and information aimed for the HoT reviewers of this excercise, in order to provide background information, explanations and my personal lessons learned to showcase how I approached this excercise and why I've done it the way it's done.

First and foremost, I have to apologize that the program doesn't work. When I approached the 7th hour of working on this project, I've deciced that I'll rather deliver it in the state it is, even though I could have spend additional 4-6 hours getting it to work.
My reasoning behind this is, that within the assignment's description it was stated that it should take approximately 5 hours to finish. While I could have worked on the assignment more and further, I believe it wouldn't be a proper showcase of my current coding skills.

I also decided not to use the help of "AI" tools. While I do consider the ability to use Qodo or Copilot effectively an important skill to have/gain, with my current level of python skills I believe it would be more of a detriment than a positive to use these tools extensively. But maybe it's also because I do enjoy understanding the background und underlying elements of coding that just "getting it done asap"

If I may, I'll also add here my notes and lessons learned to showcase how I would approach this assignment, but I'll fully accept if these are not considered during the evaluation process. The notes and comments within the code itself could be devided as personal notes to myself for stuff I wanted to work on and as comments for anyone reviewing the code.

Current issues:
1, The screen states aren't all set up and don't properly loop back, the goal was to have:
main screen -> can quit the game or choose game mode 1 or game mode 2
game mode 1 screen -> gives the human player the option to choose a valid RPS value and go to game result screen or return to main screen
game mode 2 screen -> goes to game result screen as the game is automated in this case
game result screen -> displays the game results and played RPS_values, allows for rematch either by returning to game mode 1 screen or automatically replaying (return to game mode 2 doesn't make sense). Can return to main screen as the third option
game error screen -> In case an invalid input is entered tells the user to choose a correct option and goes to main screen
2, In order to optimize, event.wait() was planned to be used in order to wait on inputs from the user and only after input continue with game logic loop. This led to looping errors that I sadly didn't have time to solve
3, print() statements have been commented in and could have been cleaned out
4, The used functions are currently defined mostly in main.py file, it would be better to create separate .py file to house the screen functions even in the current state of code (see below for ideas for a better solution)

Lessons learned:
1, At the start I decided to first implement a text based version of the game, thinking using buttons/pictures would be more complicated. However since sprites as well as blits doesn't support multiline rendering of text, the work go display the text was almost the same as starting with buttons.
2, I started to work with the main game loop in the main() function and afterwards expanded to different screens. As I generally notice an error with coding principle the moment I copy-paste a part of code 2-3 times, I realized the implementation should have been handled differently, with two possible solutions coming to mind:
Either create a class that would be a screen, with its constructor __init__() having a parametrized input of to be rendered buttons/sprites/text to show the player and handle the game logic via class specific functions, or make us of pygame's sprite.Group()-s to handle what is being rendered during runtime and thus basically have only one screen that dynamically changes based of user inputs.
3, As mentioned in point 2, the moment I copy paste some part of the code 2-3 times, I start to think about how to create a help function. Even in the current code state I should have moved several functions to a separate .py file and import it, as the main.py is bloated and should be cleaned up
4, I did enjoy the challenge, but I think my approached with nested loops isn't necesserily correct, and definitely isn't ideal. For instance, with the class based approach the main() could have simply called the main screen init function, which then would start it's own loop and based on user inputs would terminate it's own loop and init a different screen with its own loop. I haven't fully reviewed this idea so I'm not completely sure of it's feasibility, but it would definitely be more scaleable
5, Writing proper comments and explaining my though process took more time than I expected.

Thank you for reading this and reviewing my work, after I move further with boot.dev course I'd like to return to this excercise and refactor and finish it, because I did enjoy coding after a long time of non-technical work.