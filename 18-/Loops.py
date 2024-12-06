# The're 2 types of loops:
# for loop and while loop.
# The For Loop: Which is used when we
# know how many times the loop will execute.
# The While Loop: When we don't know how many times,
# but want to continue until a certain condition is not true

number = 7
user_input = input("Would you like to play? (Y/n)")

while user_input != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) ==1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")

    user_input = input("Would you like to play? (Y/n")