# Tunnels and Dragons

## Overview
Tunnels and Dragons is a simple text-based Python game created as a learning exercise to practice control flow, user input, and basic program structure. The player finds themselves lost underground and must choose between two tunnels, one of which may contain a dragon. Depending on the player’s choices, the game branches into different outcomes.

This project was intentionally kept small and focused so I could concentrate on logic, readability, and debugging rather than complexity.
This was actually one of my first programs created, so I really enjoyed making this one as it is a game, even without graphics to go along with it. 

---

## How the Game Works
- The program randomly assigns a dragon to one of two tunnels.
- The user is prompted to choose either tunnel 1 or tunnel 2.
- If the chosen tunnel contains a dragon, the user must decide whether to fight or flee.
- The game responds based on the user’s decisions and validates basic input.

---

## What I Learned
This project helped reinforce several core Python concepts:

- Using `while` loops to validate user input
- Writing nested `if / elif / else` statements correctly
- Handling string input and normalizing user responses
- Using Python’s `random` module for basic game logic
- Debugging syntax and indentation errors in a local IDE
- Moving a local Python script into version control using Git and GitHub

One of the biggest takeaways for me was understanding how small indentation or logic mistakes can break a program, even when it looks correct at first glance.

---

## How to Run
1. Make sure Python 3 is installed
2. Clone the repository
3. Run the script from the project folder:

```bash
python tunnel_game.py
