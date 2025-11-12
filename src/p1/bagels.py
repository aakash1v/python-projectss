import random

ATTEMPT_LIMIT = 10
GUESS_NUMBER = random.randint(100, 999)
WANT_TO_PLAY_AGAIN = True

a = GUESS_NUMBER // 100
b = (GUESS_NUMBER // 10) % 10
c = GUESS_NUMBER % 10

# print(GUESS_NUMBER)
# print(a, b, c)


def check_number(d1: int, d2: int, d3: int) -> str:
    if a == d1 and b == d2 and c == d3:
        return "You got it!"

    clues = ""
    for i in [d1, d2, d3]:
        if i == a:
            clues += "Femi "
        elif i in [a, b, c]:
            clues += "Pico "
        else:
            clues += "Bangles "

    return clues


def main():
    global WANT_TO_PLAY_AGAIN

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

            result = check_number(d1, d2, d3)
            print(result)
            if result == "You got it!":
                break

        print("Do you want to play again? (yes or no)")
        is_user_want_to_play = input(">")

        if is_user_want_to_play.strip().lower() not in [
            "yes",
            "y",
            "ok",
            "sure",
            "yup",
            "yeah",
        ]:
            WANT_TO_PLAY_AGAIN = False

    print("Thanks for playing!")


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
