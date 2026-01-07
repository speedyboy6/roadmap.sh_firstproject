import random

def play_round(high_score):
    print("\n" + "="*30)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    if high_score < float('inf'):
        print(f"Current Session High Score: {high_score} attempts")

    # Difficulty selection
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    
    choice = input("Enter your choice: ")
    chances = {"1": 10, "2": 5, "3": 3}.get(choice, 5)
    level = {"1": "Easy", "2": "Medium", "3": "Hard"}.get(choice, "Medium")

    print(f"\nGreat! Selected: {level}. Let's start!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You won in {attempts} attempts.")
                return attempts # Return score to update high score
            
            hint = "greater" if secret_number > guess else "less"
            print(f"Incorrect! The number is {hint} than {guess}.")
            print(f"Chances remaining: {chances - attempts}")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame Over! The number was {secret_number}.")
    return float('inf')

def main():
    session_high_score = float('inf')
    
    while True:
        score = play_round(session_high_score)
        
        # Update high score if the current round was better
        if score < session_high_score:
            session_high_score = score
            print("New Personal Best!")

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
