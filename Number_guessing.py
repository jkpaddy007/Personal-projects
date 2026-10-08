import random

def play_game():
secret_number = random.randint(1, 100)
attempts = 0

print("\n===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

def main():
while True:
play_game()

    again = input("Play again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thanks for playing!")
        break

if name == "main":
main()
