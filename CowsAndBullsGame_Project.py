import random

def no_duplicates(num):
    return len(set(str(num))) == 4

def generate_number():
    while True:
        num = random.randint(1000, 9999)
        if no_duplicates(num):
            return num

def bulls_cows(num, guess):
    bulls = cows = 0
    num_digits = list(str(num))
    guess_digits = list(str(guess))

    for i in range(4):
        if guess_digits[i] == num_digits[i]:
            bulls += 1
        elif guess_digits[i] in num_digits:
            cows += 1

    return bulls, cows

def play_game():
    num = generate_number()
    tries = int(input('Enter number of tries: '))

    while tries > 0:
        guess = int(input("Enter your guess: "))
        if not 1000 <= guess <= 9999 or not no_duplicates(guess):
            print("Invalid guess. Try again.")
            continue

        bulls, cows = bulls_cows(num, guess)
        print(f"{bulls} bulls, {cows} cows")

        if bulls == 4:
            print("You guessed right!")
            return
        tries -= 1

    print(f"You ran out of tries. Number was {num}")

play_game()