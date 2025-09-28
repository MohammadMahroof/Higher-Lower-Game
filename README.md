# Higher-Lower-Game

A fun and interactive text-based Python game where players guess which account has more followers. Inspired by popular social media follower comparison games, this project demonstrates Python basics including loops, functions, data handling, and user input.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Highlights](#code-highlights)
- [Contributing](#contributing)
- [FAQs](#faqs)
- [Project Status](#project-status)
- [License](#license)
- [Author](#author)


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


## Project Structure

| File/Folder         | Description                                         |
|---------------------|-----------------------------------------------------|
| `main.py`           | Main game script to run the game                     |
| `gamedata.py`       | Contains the dataset of accounts used for comparison |
| `art.py`            | Contains ASCII art such as game logos                 |
| `README.md`         | Project documentation                                 |
| `LICENSE`           | License file (e.g., MIT License)                      |
| `.gitignore`        | Git ignore rules for Python projects                  |
| `requirements.txt`  | (Optional) Python dependencies list                   |


## Code Highlights
- ```compare_followers(a, b)```: Compares follower counts between two accounts.
- ```format_data(account):``` Returns formatted account info for display.
- Game loop handles score tracking and repeats until incorrect guess.


## Contributing
Feel free to fork this repo and submit pull requests to improve the game with new features, data, or enhancements!


## FAQs

**Q: What data source is used for the accounts?**  
A: The accounts come from a predefined list in the game data included in the project.

**Q: Can I add more accounts to the game?**  
A: Yes, you can add additional accounts to the data list within the project files.

**Q: Does this game support a graphical interface?**  
A: Currently, it is a text-based game but could be extended with libraries like Pygame.

**Q: What Python version is required?**  
A: Python 3.x is required.


## Project Status

This project is stable and fully functional as a basic text-based game. Future enhancements may include adding more data, improving user input handling, and adding a graphical user interface.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Author
- Mohammad Mahroof
- Email: mohammadmahroof29@gmail.com
