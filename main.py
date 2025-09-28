#Display art
from art import logo, vs
from game_data import data
import random
import os

def clear_screen():
   """Use to clear the screen"""
   os.system('cls' if os.name == 'nt' else 'clear')

def compare(followers_a, followers_b):
    """Returns the account with the higher follower count."""
    if  followers_a > followers_b:
        return account_A
    else:
        return account_B
    
def format_data(account):
    """ Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."


print(logo)
score = 0
game_over = True

# Generate a random account from game data
account_A = random.choice(data)
account_B = random.choice([e for e in data if e != account_A])

# Make the game repeatable.
while game_over:
    # Display accounts to compare.
    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against B: {format_data(account_B)}")
    
    # Ask user for a guess.
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Clear the screen
    clear_screen()
    print(logo)
    
    # Get follower counts.
    A_follower_count = account_A["follower_count"]
    B_follower_count = account_B["follower_count"]
    
    # Determine the winner
    winner = compare(A_follower_count, B_follower_count)

    # Check if the player's guess is correct.
    if (player_choice == "a" and winner == account_A) or (player_choice == "b" and winner == account_B):
        score += 1
        account_A = winner # carry forward the winner.
        account_B = random.choice([e for e in data if e != account_A])
        
        print(f"You're right! Current score: {score}")
    else:
        clear_screen()
        print(logo)
        print(f"You're wrong! Your final score: {score}")
        game_over = False
