# Tic-Tac-Toe Game in Python

A simple yet engaging Tic-Tac-Toe game implemented in Python, designed to test and improve your coding skills. This project provides a structured approach to building a functional tic-tac-toe game, complete with pseudocode, design patterns, and minimalistic coding practices.

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)] [![License](https://img.shields.io/badge/license-MIT-green.svg)] [![GitHub stars](https://img.shields.io/github/stars/PartORG/python-coding-challenge?style=social)] [![GitHub forks](https://img.shields.io/github/forks/PartORG/python-coding-challenge?style=social)]

## Introduction

This project aims to create a simple yet functional Tic-Tac-Toe game using Python. It provides a structured approach to building the game, including pseudocode, design patterns, and minimalistic coding practices. The goal is to help you understand the basics of game development in Python while adhering to best coding standards.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Technology Stack](#technology-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development](#development)
- [Limitations](#limitations)
- [License](#license)

## Features

### Minimalistic Coding Practices

- **Explicit Function Names:** Functions have clear and descriptive names.
- **Docstrings:** Each function includes a docstring explaining its purpose and usage.
- **Function Length:** Functions are kept between 4-10 lines of code for better readability.

### Modular Design

- **Separate Modules:** The game is divided into several modules (`board.py`, `logic.py`, `player.py`) to promote modularity and reusability.

## How It Works

The Tic-Tac-Toe game follows a simple workflow:

1. **Initialize the Board:** The board is created using a 3x3 grid.
2. **Player Input:** Players take turns entering their moves.
3. **Game Logic:** The logic module checks for win conditions and determines if the game has ended.
4. **Display Results:** The final state of the board and the result (win, lose, or draw) are displayed.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming language used to implement the game logic. |
| Virtual Environment | Manages dependencies and ensures consistent development environments. |

## Requirements

- **Python:** Version 3.11 or higher.
- **Virtual Environment:** `pyenv` is recommended for managing Python versions.

## Installation

To set up your environment, follow these steps:

### macOS

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

### WindowsOS (PowerShell)

```powershell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

### WindowsOS (Git-Bash)

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
pip install --upgrade pip
```

If you encounter an error when running `pip install --upgrade pip`, try using:

```bash
python.exe -m pip install --upgrade pip
```

## Configuration

No configuration files are required for this project.

## Quick Start

To run the game, execute the following command:

```bash
python tic_tac_toe.py
```

This will start the Tic-Tac-Toe game in your terminal.

## Usage

Here is a basic example of how to play the game:

1. **Initialize the Game:**

    ```python
    from board import Board
    from logic import Logic
    from player import Player

    board = Board()
    logic = Logic(board)
    player1 = Player('X')
    player2 = Player('O')

    current_player = player1
    ```

2. **Game Loop:**

    ```python
    while not logic.is_game_over():
        print(board)
        move = input(f"{current_player.symbol}'s turn (row, col): ")
        row, col = map(int, move.split(','))
        if board.make_move(row, col, current_player.symbol):
            if logic.check_winner(current_player.symbol):
                print(f"Player {current_player.symbol} wins!")
                break
            elif logic.is_draw():
                print("It's a draw!")
                break
            current_player = player2 if current_player == player1 else player1

    print(board)
    ```

## Project Structure

```
.
├── .gitignore
├── Examples/
│   ├── README.md
│   └── script1.py
│       └── script2.py
├── Intro_to_pseudocode.md
├── LICENSE
├── README.md
├── Tic-Tac-Toe-assignment.md
├── board.py
├── logic.py
├── player.py
├── program_design.md
└── tic_tac_toe.py
└── tic_tac_toe_pseudocode.txt
```

- **Examples/**: Contains example scripts demonstrating the use of `if __name__ == '__main__':`.
- **Intro_to_pseudocode.md**: Provides an introduction to pseudocode.
- **LICENSE**: MIT License file.
- **README.md**: This document.
- **Tic-Tac-Toe-assignment.md**: Assignment details and guidelines.
- **board.py**: Contains the `Board` class for managing the game board.
- **logic.py**: Contains the `Logic` class for game logic.
- **player.py**: Contains the `Player` class for player management.
- **program_design.md**: Describes the design patterns used in the project.
- **tic_tac_toe.py**: Main entry point of the game.

## Development

To contribute to this project, follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive messages.
5. Push your changes to your forked repository.
6. Open a pull request to merge your changes into the main branch.

## Limitations

- The game does not support multiplayer over the network.
- No graphical user interface (GUI) is included.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.