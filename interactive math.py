import random

def math_quiz_game():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    print(f"What is {num1} + {num2}?")
    guess = int(input("Your answer: "))
    
    if guess == correct_answer:
        print("Correct! Well done!")
    else:
        print(f"Oops! The correct answer is {correct_answer}")

def color_guessing_game():
    colors = ["red", "blue", "green", "yellow"]
    chosen_color = random.choice(colors)
    print(f"Guess the color from: {', '.join(colors)}")
    guess = input("Your guess: ").lower()
    
    if guess == chosen_color:
        print("You guessed it right!")
    else:
        print(f"Oops! The correct color was {chosen_color}")

def play_game():
    print("1. Math quiz game")
    print("2. Color guessing game")
    choice = int(input("Pick a game (1 or 2): "))
    
    if choice == 1:
        math_quiz_game()
    elif choice == 2:
        color_guessing_game()
    else:
        print("Invalid choice. Please select 1 or 2.")
    
    again = input("Do you want to play again? (yes/no): ").lower()
    
    if again == "yes":
        play_game()
    else:
        print("Goodbye!")

# Start the game
play_game()
