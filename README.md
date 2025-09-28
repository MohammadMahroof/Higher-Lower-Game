# Higher-Lower-Game

A fun and interactive text-based Python game where players guess which account has more followers. Inspired by popular social media follower comparison games, this project demonstrates Python basics including loops, functions, data handling, and user input.

## Features
- Randomly selects two accounts for comparison from a dataset
- Displays formatted account information (name, description, country)
- Asks the player to guess which account has more followers
- Tracks and displays the current score for correct guesses
- Provides feedback on right or wrong answers
- Clears the screen for smooth user experience
- Replayable game loop until the player guesses incorrectly


## Technologies Used
- Python 3
- Standard libraries: ``` random, os ``` 
- Data handled via lists and dictionaries


## Installation
1. Clone the repository:
```bash
git clone https://github.com/MohammadMahroof/higher-lower-game.git
cd higher-lower-game
```
2. Make sure Python 3 is installed on your system.

3. (Optional) Create a virtual environment and activate it:
```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate
```

## Usage
Run the game script from the command line:
```bash
python main.py
Follow the on-screen instructions to play the game. Type "A" or "B" to guess which account has the higher follower count.
```

## Code Highlights
- ```compare_followers(a, b)```: Compares follower counts between two accounts.
- ```format_data(account):``` Returns formatted account info for display.
- Game loop handles score tracking and repeats until incorrect guess.


## Contributing
Feel free to fork this repo and submit pull requests to improve the game with new features, data, or enhancements!


## Author
- Mohammad Mahroof
- Email: mohammadmahroof29@gmail.com
