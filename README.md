# TIC-TAC-TOE
✅ Project Title:
Tic-Tac-Toe AI using Minimax Algorithm

✅ Description:
This project involves building an AI agent that plays the classic game of Tic-Tac-Toe against a human player. The AI uses the Minimax algorithm, a popular game theory algorithm, to make perfect decisions and become unbeatable.

The game is played on a 3×3 grid where two players take turns marking the spaces — the human is assigned X, and the AI uses O. The goal is to place three of the same marks in a row, column, or diagonal.

The Minimax algorithm enables the AI to simulate all possible future moves, assuming that the opponent plays optimally. It recursively calculates the best move by maximizing the AI's chances of winning and minimizing the human's chances. This way, the AI always chooses the move that leads to a win or draw, never a loss.

✅ Key Features:
Fully playable Tic-Tac-Toe game in the terminal.

Human vs AI interaction.

AI is unbeatable using Minimax logic.

Detects win, loss, and draw scenarios automatically.

Clean and simple code using basic Python (no external libraries).

✅ Technologies Used:
Python (Core)

Minimax Algorithm

No machine learning or external libraries required

✅ How It Works:
The game board is stored as a list of 9 cells.

The Minimax function explores every possible move to choose the best outcome.

When it's the AI’s turn, it:

Checks all possible moves.

Recursively simulates future moves of the player.

Chooses the move that leads to the highest possible score.

Human inputs move using numbers 1–9.

✅ What I Learned (Self-Learning Outcomes):
How to implement game logic using Python.

The working of the Minimax algorithm.

Basics of game trees, recursion, and search strategies.

How to structure a turn-based interactive game.
✅ Advantages of This Model:
No randomness — AI always makes the best move.

Helps in understanding the basics of AI logic without ML.

Builds a strong foundation in game theory and search algorithms.

✅ Limitations:
Only supports 3x3 grid (classic version).

No GUI (text-based only).

Can be slow if extended to larger boards without optimization.

✅ Future Improvements:
Add Alpha-Beta Pruning to optimize the AI’s decision-making speed.

Create a Graphical User Interface (GUI) using Tkinter or Pygame.

Add difficulty levels (Easy, Medium, Hard) by limiting AI depth
