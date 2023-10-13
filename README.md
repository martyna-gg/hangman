# Hangman

Hangman game with usage of random module, lists, if/else/elif statements, while loop, loop control statements, reading files and processing user input.

## Installation

Random module is a python built-in module. No installation is required.

## Requirements

Code was developed and tested using: 

Ubuntu 18.04.6 LTS 

Python 3.6.9

## Usage

The game starts with menu with three options: play a game, see the results or exit.

Results. Shows the results of all games played during this program run.

```
$ python3 hangman.py
H A N G M A N 

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >results

You won: 0 times. 
You lost: 0 times.

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >

```

Play a game. Player has to guess a randomly selected word. Word is pictured by a game board where every unguessed letter is represented by underscore. 

```
$ python3 hangman.py
H A N G M A N 

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >play

-----

Input a letter: >

```

In every turn player points a letter that is in the word. There might be eight misses. Everytime the chosen letter appears in the word the letter is uncovered in the game board. Otherwise, an appropriate message is displayed.

```
Input a letter: > r

---------

That letter doesn't appear in the word.

Input a letter: > t

-------t-

Input a letter: >

```

The game ends when all letters are guessed or there were eight misses.

```
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:play
---

Input a letter: > a
a--

Input a letter: > n
an-

Input a letter: > d
and

You guessed the word and! 
You survived!

```

```
H A N G M A N 

Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >play

-----

Input a letter: > e

-----

That letter doesn't appear in the word.

Input a letter: > r

-----

That letter doesn't appear in the word.

Input a letter: > g

-----

That letter doesn't appear in the word.

Input a letter: > y

-----

That letter doesn't appear in the word.

Input a letter: > a

----a

Input a letter: > d

----a

That letter doesn't appear in the word.

Input a letter: > q

----a

That letter doesn't appear in the word.

Input a letter: > h

----a

That letter doesn't appear in the word.

Input a letter: > l

----a

That letter doesn't appear in the word.

You lost! The keyword to guess was: pucka

```

## Support

If you face any problem let me know by Issue.

## Roadmap

In the future I plan a release with difficulty levels added.