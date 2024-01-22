import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper") 
    ):
        return "You win!"
    else:
        return "Computer wins!"
    
def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter a choice (rock, paper, scissors): ")
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"You chose {user_choice.capitalize()}.")
        print(f"Computer chose {computer_choice.capitalize()}.")
    
        result = determine_winner(user_choice, computer_choice)
        print(result)


        if "You" in result:
            user_score += 1
        elif "Computer" in result:
            computer_score += 1
        
        
        print(f"Score: You {user_score} - {computer_score} Computer ")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()