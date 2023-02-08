# Matchmaking-System-for-Games


> In multiplayer games, matchmaking is the process of connecting players together for online play sessions. 
In this project we are trying to make a matchmaking system for a game of guessing numbers.
Assuming that player wants to play with maximum number in mind with certain number of tries. 
Some people wants to be guesser where some wants to be decider.


### Required Modules
1. `socket` : Create the client and connect to local host.
2. `threading` : Create a new thread to match between clients (guesser/decider).

### Components of matchmaking
* tries : In how many tries you want to guess it.
* maximum number = What is the limit of number to be guessed.
* role : You can be a guesser or a decider.
* guesser : Guesser will guess the number which already inputted by the decider.
* decider : It wil decide what number guesser must guess.

### Working Methodology 
> Firstly we ask user about how many tries they want then what is the maximum number then what they want to be (guesser/decider). 
In matchmaking the `match` will only appear when two players have differnt roles one will be the guesser and one will be the decider. 
For working with this methodology we created two files: <br />
1. `game_server.py` <br />
2. `game_client.py` <br />

This matchmaking system is for number guessing game we can have many players in this game and then the matchmaking begins.


