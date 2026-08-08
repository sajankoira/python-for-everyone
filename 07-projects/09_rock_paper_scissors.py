"""
PROJECT 9: Rock Paper Scissors + Dice Roller
"""
import random

def dice_roller():
    print("\n🎲 Dice Roller")
    while True:
        input("Press Enter to roll (q to quit): ")
        dice = random.randint(1,6)
        print(f"You rolled: {dice} {'⚀⚁⚂⚃⚄⚅'[dice-1]}")
        if input("Continue? (y/n): ").lower() != 'y':
            break

def rock_paper_scissors():
    print("\n✊✋✌️ Rock Paper Scissors")
    choices = ["rock", "paper", "scissors"]
    win_rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    user_score = comp_score = 0
    
    while True:
        print(f"\nScore - You: {user_score} | Computer: {comp_score}")
        user = input("Choose rock/paper/scissors (or q to quit): ").lower()
        
        if user == 'q':
            break
        if user not in choices:
            print("Invalid choice!")
            continue
        
        comp = random.choice(choices)
        print(f"You: {user} vs Computer: {comp}")
        
        if user == comp:
            print("Tie! 🤝")
        elif win_rules[user] == comp:
            print("You win! 🎉")
            user_score += 1
        else:
            print("You lose! 😢")
            comp_score += 1
    
    print(f"\nFinal Score - You: {user_score} | Computer: {comp_score}")
    if user_score > comp_score:
        print("🏆 You are overall winner!")
    elif user_score < comp_score:
        print("Computer wins overall!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    print("Games Menu:")
    print("1. Dice Roller")
    print("2. Rock Paper Scissors")
    ch = input("Choose 1 or 2: ")
    if ch == "1":
        dice_roller()
    elif ch == "2":
        rock_paper_scissors()
    else:
        print("Running both demo:")
        dice_roller()
