import random

ATTEMPT_LIMIT = 10
GUESS_NUMBER = random.randint(100, 999)
WANT_TO_PLAY_AGAIN = True 

a = GUESS_NUMBER // 100
b = (GUESS_NUMBER // 10) % 10
c = GUESS_NUMBER % 10

print(GUESS_NUMBER)
print(a, b, c)


def check_number(d1: int, d2: int, d3: int) -> str:

    if a == d1 and b == d2 and c == d3:
        return "You got it!"

    result = ""
    for i in [d1, d2, d3]:
        print(i)
        if i == a:
            result += "Femi "
        elif i in [a, b, c]:
            result += "Pico "
        else: 
            result += "Bangles "

    return result


print("**** Bagels, a deductive logic game. ****")
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("""
\tWhen I say: That means:
\tPico One digit is correct but in the wrong position.
\tFermi One digit is correct and in the right position.
\tBagels No digit is correct.\n
""")

print(
    "I have thought up a number.\
You have 10 guesses to get it.\
"
)

while WANT_TO_PLAY_AGAIN:
    for i in range(1, ATTEMPT_LIMIT + 1):
        print(f"Guess #{i}:")
        mynumber = input(">")
        try:
            # This splits the string AND converts each character to an int
            d1, d2, d3 = map(int, mynumber)

        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Please enter exactly 3 digits.")
            continue

        display_string = check_number(d1, d2, d3)
        print(display_string)
        if display_string == "You got it!":
            break

    print("Do you want to play again? (yes or no)")
    is_user_want_to_play = input(">")

    if is_user_want_to_play not in ["yes", "y", "ok", "sure", "yup"]:
        WANT_TO_PLAY_AGAIN = False


print("Thanks for playing!")
