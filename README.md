# Live Football World Cup Scoreboard

The Live Football World Cup Scoreboard is a library that provides functionality to track ongoing football matches and their scores.

## Features

The library supports the following operations:

1. Start a new game: Initialize a new match with an initial score of 0-0 and add it to the scoreboard.
2. Update score: Modify the score of a match with the provided home team score and away team score.
3. Finish game: Remove a match from the scoreboard that has finished.
4. Get summary: Retrieve a summary of ongoing matches ordered by their total score, with ties being ordered by the most recently started match.

## Usage

```python
from scoreboard import Scoreboard

scoreboard = Scoreboard()

# Start a new match
scoreboard.start_game("Mexico", "Canada")

# Update the score of a match
scoreboard.update_score(0, 5, 0)

# Finish a match
scoreboard.finish_game(0)

# Get the summary of ongoing matches
summary = scoreboard.get_summary()
for match_summary in summary:
    print(match_summary)
```

## Requirements
Python 3.x

## Installation
* Clone the repository: git clone https://github.com/your_username/football-scoreboard.git
* Change to the project directory: cd football-scoreboard
* Use the library in your code by importing scoreboard module.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.