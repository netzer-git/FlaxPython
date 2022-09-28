# FlaxPython

Hi! That's a very vanilla-cli version of Marvel Snap - the (amazing) phone card game.
This game was built in unprofessional hands, as a school and private project, and it's not on for commercial use.
Let's be real, the real game is so much fun.

### First Stage : Vanilla Game

On the first stage I want to create the game, with easy (and not very nice) cli ux\ui. The vanilla version of the game
contains just vanilla cards and areas - no special powers at all.
Running the game can be done in main.py file - that's runs some of the configurations and then runs the game.

Game logs can be found in the debug folder. I tried to use custom tags for the logs, the tags recorded in
debug/tags.txt.

Since the game can be a bit tedious to play over and over, I created an input wrapper for the game input. The wrapper is
old-fashioned and it works. You have to pay attention though that the pre-scripted steps rely on what cards the player
have in his hands. Currently, the player's decks are entered at main.py, but I hope to change it in the future (and add
an option to run specific script with specific decks).

So. for now we have: vanilla running game, logs and scripted-games.

### Second Step : Real Game

The next step is the one that I'm always struggling with in card games - how to add special and game breaking powers to
specific\unique cards. So, when I designed this code (even if it's looks very messy), this thought was always in my
mind.

The main idea is: the all-knowing Game is a singleton. This way each card and area can use special function in a way
that the function accesses the Game singleton and changes it as needed.

So second step is making the game real. Fun. Maybe even a bit different than the original version.

(By the way, I'm sure not going to make all the cards in the game - there are crazy powers that I have no idea how to
remake)

### Third Stage : Bot Time

And here comes the real deal. The unknown. The part that I'm actually want to learn - how to make a game learn to play
FlaxPython. Good luck.

