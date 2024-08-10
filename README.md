# Ping Pong Style Game

This is a simple two-player Ping Pong style game developed using Python's Tkinter library. The game is designed and tested for macOS. It allows two players to control paddles and hit a ball back and forth on a virtual ping pong table.

## Prerequisites

Before running the game, ensure you have the following:

- **Python 3.x** installed on your system.
- **Tkinter** library (typically included with Python installations).

## Getting Started

### 1. Download the Script
### 2. Run the Game

1. Open a terminal window.
2. Navigate to the directory where your script is saved.
3. Run the game by typing the following command:

   ```bash
   python3 ping_pong_game.py
   ```

4. The game window should open, displaying the welcome screen.

### 3. Start Playing

1. Click the "Start Game" button to begin the game.
2. Player 1 (Left) controls their paddle using the **'W'** (up) and **'S'** (down) keys.
3. Player 2 (Right) controls their paddle using the **'↑'** (up) and **'↓'** (down) arrow keys.
4. The goal is to prevent the ball from passing your paddle.

## Explanation of the Code

- **Outer and Inner Loops**:
    - `outerloop()`  initializes the game and displays the welcome screen.
    - `innerloop()`  starts the game by setting up the game window and elements.

- **Game Elements**:
    - **Canvas**: A `Canvas` widget is used to draw the game elements, including the paddles and the ball.
    - **Paddles (Buttons 1 and 2)**: These are controlled by the players using specific keyboard keys.
    - **Ball**: The ball moves across the screen, and bounces off the paddles and screen edges.

- **Collision Detection**:
    - The game includes logic to detect collisions between the ball and paddles, which causes the ball to bounce back.

- **Score Tracking**:
    - Scores for both players are tracked and displayed on the screen.

- **Exit Button**:
    - An "Exit Game" button allows players to quit the game and return to the welcome screen.

## Notes

- **Platform**: The game should work on other platforms that support Python and Tkinter, but some adjustments may be needed.
- **Game Speed**: The game speed is controlled using `time.sleep(0.005)` in the `run_game()` loop. Adjust this value if the game runs too fast or too slow on your system.

## Troubleshooting

- **Game Not Starting**:
    - Ensure that Python 3.x is installed and that you are running the script using `python3`.
    - Verify that Tkinter is installed on your system.

- **Paddles Not Moving**:
    - Make sure the game window is active and selected while pressing the control keys.

## References

- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
