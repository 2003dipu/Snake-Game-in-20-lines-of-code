import random
print('Welcome to number guessing game where you set the hightest number and computer\
 generates a number randomly between lowest and the highest number you set.')
print("---------------------------   Let's begin  ------------------------------------------------------------")
lowest_number = int(input('Set the lowest number: '))
highest_number = int(input('Set the highest number: '))
guesses = 0
number = random.randint(lowest_number, highest_number)

while True:
    guess = int(input(f"Enter a number between ({lowest_number} - {highest_number}): "))
    guesses += 1

    if guess > number:
        print(f"{guess} is too high.")
    elif guess < number:
        print(f"{guess} is too low")
    else:
        print(f"{guess} is correct! ")
        print("----------------You Win ------------")
        break
print(f"This round took you {guesses} guesses to guess the number computer randomly generated.!")