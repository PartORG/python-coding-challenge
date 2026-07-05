# Tic-Tac-Toe Game in Python

A simple yet engaging Tic-Tac-Toe game implemented in Python, designed to test and improve coding skills. This project includes a structured development workflow, comprehensive documentation, and a set of guidelines for writing clean and maintainable code.

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)] [![License](https://img.shields.io/badge/license-MIT-green.svg)] [![GitHub stars](https://img.shields.io/github/stars/PartORG/python-coding-challenge?style=social)] [![GitHub forks](https://img.shields.io/github/forks/PartORG/python-coding-challenge?style=social)]

## Introduction

This project aims to create a Tic-Tac-Toe game using Python. It provides a structured approach to developing the game, including detailed documentation and coding guidelines. The repository includes various files and directories, with primary focus on Python programming.

The primary workflow involves setting up a virtual environment, installing dependencies, and following the provided pseudocode and design documents to implement the game logic in Python files such as `board.py`, `logic.py`, and `player.py`.

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

### 1. **Game Logic Implementation**
   - The game logic is implemented in the `logic.py` file, ensuring a clear and maintainable structure.
   - Functions have explicit names and docstrings for better readability and understanding.

### 2. **Board Management**
   - The `board.py` file manages the game board, providing methods to update the board state and check for win conditions.

### 3. **Player Interaction**
   - The `player.py` file handles player input and interaction with the game board.
   - Functions are designed to be concise, adhering to the guideline of being between 4-10 lines of code long.

## How It Works

The Tic-Tac-Toe game follows a straightforward workflow:

1. **Setup**: A virtual environment is created and activated.
2. **Game Loop**: The main game loop in `tic_tac_toe.py` manages turns, checks for win conditions, and updates the board state.
3. **Player Input**: Players input their moves through the command line interface.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming language used to implement the game logic. |
| virtualenv | Manages project-specific dependencies. |
| pip | Package installer for Python packages. |

## Requirements

- Python 3.11
- virtualenv

## Installation

To install and run the Tic-Tac-Toe game, follow these steps:

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

## Configuration

No specific configuration files are required for this project.

## Quick Start

To run the Tic-Tac-Toe game, execute the following command:

```bash
python tic_tac_toe.py
```

## Usage

The `tic_tac_toe.py` file contains the main entry point of the application. The game loop is managed within this file, handling player input and updating the board state.

## Project Structure

```
.
├── .gitignore
├── Examples/
│   ├── README.md
│   ├── script1.py
│   └── script2.py
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

- `Examples/`: Contains example scripts demonstrating the use of `if __name__ == '__main__':`.
- `Intro_to_pseudocode.md`: Provides an introduction to pseudocode.
- `LICENSE`: MIT License file.
- `README.md`: This document.
- `Tic-Tac-Toe-assignment.md`: Assignment description and guidelines.
- `board.py`, `logic.py`, `player.py`: Python files implementing game logic, board management, and player interaction.
- `program_design.md`: Design documents for the project.
- `tic_tac_toe.py`: Main entry point of the application.

## Development

The development workflow involves setting up a virtual environment, installing dependencies, and following the provided pseudocode and design documents to implement the game logic in Python files such as `board.py`, `logic.py`, and `player.py`.

## Limitations

- The project does not include automated testing.
- No graphical user interface is implemented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.