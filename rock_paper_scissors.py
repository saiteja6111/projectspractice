import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

# ASCII art for the choices
CHOICES_ART = {
    'rock': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    'paper': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    'scissors': '''
    _______
---'   ____)____
          ______)
   __________)
  (____)
---.__(___)
'''
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color=Fore.WHITE):
    print(f"{color}{text}{Style.RESET_ALL}")

def get_user_choice():
    while True:
        print_colored("\nChoose your weapon:", Fore.CYAN)
        print_colored("1. Rock 🪨", Fore.YELLOW)
        print_colored("2. Paper 📄", Fore.YELLOW)
        print_colored("3. Scissors ✂️", Fore.YELLOW)
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            return 'rock'
        elif choice == '2':
            return 'paper'
        elif choice == '3':
            return 'scissors'
        print_colored("Invalid choice! Please try again.", Fore.RED)

def get_computer_choice(difficulty='normal'):
    if difficulty == 'easy':
        # Computer is more likely to choose rock
        return random.choice(['rock'] * 3 + ['paper', 'scissors'])
    elif difficulty == 'hard':
        # Computer is more likely to choose the winning move
        return random.choice(['rock', 'paper', 'scissors'] * 2 + ['rock'])
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    return "Computer wins!"

def display_choices(user_choice, computer_choice):
    print("\n" + "="*50)
    print_colored("Your choice:", Fore.GREEN)
    print(CHOICES_ART[user_choice])
    print_colored("Computer's choice:", Fore.RED)
    print(CHOICES_ART[computer_choice])
    print("="*50 + "\n")

def display_stats(stats):
    print_colored("\n=== Game Statistics ===", Fore.CYAN)
    print_colored(f"Total games played: {stats['total_games']}", Fore.WHITE)
    print_colored(f"Wins: {stats['wins']}", Fore.GREEN)
    print_colored(f"Losses: {stats['losses']}", Fore.RED)
    print_colored(f"Ties: {stats['ties']}", Fore.YELLOW)
    if stats['total_games'] > 0:
        win_rate = (stats['wins'] / stats['total_games']) * 100
        print_colored(f"Win rate: {win_rate:.1f}%", Fore.CYAN)

def play_game():
    clear_screen()
    print_colored("Welcome to Rock Paper Scissors!", Fore.CYAN)
    print_colored("===============================", Fore.CYAN)
    
    # Initialize statistics
    stats = {
        'total_games': 0,
        'wins': 0,
        'losses': 0,
        'ties': 0
    }
    
    # Select difficulty
    print_colored("\nSelect difficulty:", Fore.CYAN)
    print_colored("1. Easy", Fore.GREEN)
    print_colored("2. Normal", Fore.YELLOW)
    print_colored("3. Hard", Fore.RED)
    while True:
        diff_choice = input("\nEnter difficulty (1/2/3): ").strip()
        if diff_choice in ['1', '2', '3']:
            difficulty = ['easy', 'normal', 'hard'][int(diff_choice) - 1]
            break
        print_colored("Invalid choice! Please try again.", Fore.RED)
    
    while True:
        clear_screen()
        display_stats(stats)
        
        user_choice = get_user_choice()
        print_colored("\nRock...", Fore.YELLOW)
        time.sleep(0.5)
        print_colored("Paper...", Fore.YELLOW)
        time.sleep(0.5)
        print_colored("Scissors...", Fore.YELLOW)
        time.sleep(0.5)
        print_colored("Shoot!", Fore.YELLOW)
        
        computer_choice = get_computer_choice(difficulty)
        display_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            print_colored(result, Fore.GREEN)
            stats['wins'] += 1
        elif result == "Computer wins!":
            print_colored(result, Fore.RED)
            stats['losses'] += 1
        else:
            print_colored(result, Fore.YELLOW)
            stats['ties'] += 1
        
        stats['total_games'] += 1
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    clear_screen()
    print_colored("\n=== Final Statistics ===", Fore.CYAN)
    display_stats(stats)
    print_colored("\nThanks for playing! Come back soon! 👋", Fore.CYAN)

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print_colored("\n\nGame terminated by user. Goodbye! 👋", Fore.YELLOW) 