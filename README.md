# Hangman - Revisited

It is the year 2034.
The COVID pandemic rages on.
People around the world have exhausted their supply of entertainment and are now turning to other sources to cure their boredom.
One game stands out above all others in providing people with endless joy: Hangman.

Here at Hangman Hubs, we empower strangers, friends, coworkers, families, and people that have oddly close relationships with their pets to connect to each other at a deeper level.
We do that through the classic game of hangman.

If you don’t know what hangman is, no worries!
It’s a simple word game where the player has a limited number of chances to guess a random word.

Here are the rules:

- A random word is chosen at the beginning of the game.
- The word is hidden from the player.
- The player has to guess, one letter at a time, what the word is.
- Each successful guess will reveal the letter in the hidden word.
- If they guess incorrectly 5 times, then it’s game over.
- If they guess the word correctly and the whole word is revealed, they win!

Unfortunately, the game was working until Today! It appears that the virus evolved and can now alter code. We need you to fix the game and restore balance in the world.

## The Requirements

- Implement the guess feature in the hangman server
- Update the API with a new guess endpoint that will work with the provided hangman web app

## What are we looking for?

**We don't expect this exercise to take longer than 3 hours to be completed. But please feel free to take the time you need to work on this.**

When reviewing your solution we will check:

- The feature works as described.
- All requirements are fulfilled.
- The code is of good quality.
- Some automated tests are needed.

During your in person interview, we’ll do a live code review where we’ll go over your changes and have you talk through some decisions you made while implementing the feature.
We want to see how well you can understand an existing codebase and make a meaningful change to it.

## How should you submit your solution?

Create a new branch for the feature and open a pull request once you're done

## What does this repository include?

A simple hangman ui and server using js, react, python and flask!

It's split into two projects:

- [hangman-server](hangman-server)
- [hangman-web-app](hangman-web-app)

## Getting started

Get the server up and running

```
cd hangman-server
make install
make test
make start
```

Get the web-app running

```
cd hangman-web-app
npm install
npm run start
```

Play some hangman!

```
http://localhost:3000
```

Good luck and have fun!
