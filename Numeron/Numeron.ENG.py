import random
def number_generator():
    number100 = random.randint(0,9)
    number10 = random.randint(0,9)
    number1 = random.randint(0,9)

    if (number100 == number10 or number100 == number1 or number10 == number1):
        number_generator()
        
    else:
        number = []
        number.append(number100)
        number.append(number10)
        number.append(number1)
        print(number)
        return number
number = number_generator()

def numeron(digit_list,number):
    if (digit_list[0] == number[0] and digit_list[1] == number[1] and digit_list[2] == number[2]):
        print("3 eat, game over!")
        print("you guessed it correct!")

    elif (digit_list[0] == number[0] and digit_list[1] == number[1]):
        print("2 eat, 0 bite")
        return main()

    elif (digit_list[0] == number[0] and digit_list[2] == number[2]):
        print("2 eat, 0 bite")
        return main()

    elif (digit_list[1] == number[1] and digit_list[2] == number[2]):
        print("2 eat, 0 bite")
        return main()

    elif (digit_list[0] == number[0]):
        if (number[1] in digit_list and number[2] in digit_list):
            print("1 eat, 2 bite")
            return main()

        elif (number[1] in digit_list or number[2] in digit_list):
            print("1 eat, 1 bite")
            return main()

        else:
            print("1 eat, 0 bite")
            return main()
        
    elif (digit_list[1] == number[1]):
        if (number[0] in digit_list and number[2] in digit_list):
            print("1 eat, 2 bite")
            return main()

        elif (number[0] in digit_list or number[2] in digit_list):
            print("1 eat, 1 bite")
            return main()

        else:
            print("1 eat, 0 bite")
            return main()
        

    elif (digit_list[2] == number[2]):
        if (number[0] in digit_list and number[1] in digit_list):
            print("1 eat, 2 bite")
            return main()

        elif (number[0] in digit_list or number[1] in digit_list):
            print("1 eat, 1 bite")
            return main()

        else:
            print("1 eat, 0 bite")
            return main()

    elif (number[0] in digit_list and number[1] in digit_list and number[2] in digit_list):
        print("0 eat, 3 bite")
        return main()

    elif (number[0] in digit_list and number[1] in digit_list):
        print("0 eat, 2 bite")
        return main()
        
    elif (number[0] in digit_list and number[2] in digit_list):
        print("0 eat, 2 bite")
        return main()

    elif (number[1] in digit_list and number[2] in digit_list):
        print("0 eat, 2 bite")
        return main()

    elif (number[0] in digit_list or number[1] in digit_list or number[2] in digit_list):
        print("0 eat, 1 bite")
        return main()

    else:
        print("0 eat, 0 bite")
        return main()

def main():
    print(" ")
    digit_string = str(input("what is your guess?"))
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)

    if (len(digit_list) != 3):
        print("You gave us an invalid number.")
        print("Try a three-digit number.")
        print("Please, enter a correct number.")
        main()

    elif (digit_list[0] == digit_list[1] or digit_list[1] == digit_list[2] or digit_list[2] == digit_list[0]):
        print("You gave us an invalid number.")
        print("You can't type 2 same numbers. Each number has to be different.")
        print("Please, enter a correct number.")
        main()
    print(" ")
    numeron(digit_list,number)
    
def initial():
    print("Welcome to 'Numeron 3!'")
    print("This game is a number-guessing game.")
    print("First, you will give us a random three-digit number.")
    print("Then, we will give you a feedback to guess the correct number.")
    print("Enjoy the game!")
    print(" ")
    print("Are you ready?")

    if (str(input("type yes or no: ".lower()) == "yes")):
        main()

    else:
        initial()

initial()