# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 18, 2022
# This program asks the user to guess a
# number and if they get it wrong it loops back till they get it correctly
import random


def main():
    # initialize the counter
    counter = -1
    # generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    while True:
        # Get the user input
        user_input = input("Guess the number between 0 and 9 (positive number only): ")
        try:
            # changes user input to an integer
            user_number = int(user_input)
        except Exception:
            print("{} is a string".format(user_input))
            print()
            continue
            # Check to see if they inputted a above or equal to 0
            # and checks to see it it exceeds 9
        if user_number >= 0 and user_number <= 9:
            counter = counter + 1
            if user_number == random_number:
                # Display result to user
                print()
                print("YOU GUESS IT CORRECTLY.")
                print("Thanks for playing")
                break
            # checks to see if user got the number wrong or right
            else:
                # Display result to user
                print("THIS IS THE WRONG GUESS, TRY AGAIN.")
                print()
        else:
            print("THIS IS NOT BETWEEN 0 AND 9.")
            print()



if __name__ == "__main__":
    main()
