##Numeron game
##1. import a random 3 digits number
##2. ask the user thier guess of the computer's number
##3. continue asking until the user get the right number
##4. print("You guessed it!") when the user get the right number
## digit_list = user input, number = answer
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


        return number

number = number_generator()


def numeron(digit_list,number):

    # 3 eat and game over ---> No change
    if (digit_list[0] == number[0] and digit_list[1] == number[1] and digit_list[2] == number[2]):
        print("3 イート")
        print("見事正解しました！")

    
    # 2 eat, 0 bite ---> No change
    elif (digit_list[0] == number[0] and digit_list[1] == number[1]):
        print("2 イート, 0 バイト")
        return main()

    elif (digit_list[0] == number[0] and digit_list[2] == number[2]):
        print("2 イート, 0 バイト")
        return main()

    elif (digit_list[1] == number[1] and digit_list[2] == number[2]):
        print("2 イート, 0 バイト")
        return main()
    
    # 1 eat, n bite
    elif (digit_list[0] == number[0]):
        # 2 bite
        if (number[1] in digit_list and number[2] in digit_list):
            print("1 イート, 2 バイト")
            return main()

        # 1 bite
        elif (number[1] in digit_list or number[2] in digit_list):
            print("1 イート, 1 バイト")
            return main()

        # 0 bite
        else:
            print("1 イート, 0 バイト")
            return main()


        
    elif (digit_list[1] == number[1]):
        # 2 bite
        if (number[0] in digit_list and number[2] in digit_list):
            print("1 イート, 2 バイト")
            return main()

        # 1 bite
        elif (number[0] in digit_list or number[2] in digit_list):
            print("1 イート, 1 バイト")
            return main()

        # 0 bite
        else:
            print("1 イート, 0 バイト")
            return main()
        

    elif (digit_list[2] == number[2]):
        # 2 bite
        if (number[0] in digit_list and number[1] in digit_list):
            print("1 イート, 2 バイト")
            return main()

        # 1 bite
        elif (number[0] in digit_list or number[1] in digit_list):
            print("1 イート, 1 バイト")
            return main()

        # 0 bite
        else:
            print("1 イート, 0 バイト")
            return main()

    # 0 eat, 3 bite
    elif (number[0] in digit_list and number[1] in digit_list and number[2] in digit_list):
        print("0 イート, 3 バイト")
        return main()

    # 0 eat, 2 bite
    elif (number[0] in digit_list and number[1] in digit_list):
        print("0 イート, 2 バイト")
        return main()
        
    elif (number[0] in digit_list and number[2] in digit_list):
        print("0 イート, 2 バイト")
        return main()

    elif (number[1] in digit_list and number[2] in digit_list):
        print("0 イート, 2 バイト")
        return main()

    # 0 eat, 1 bite ---> No change
    elif (number[0] in digit_list or number[1] in digit_list or number[2] in digit_list):
        print("0 イート, 1 バイト")
        return main()


    # 0 eat, 0 bite ---> No change
    else:
        print("0 イート, 0 バイト")
        return main()
        
        
    



def main():

    print(" ")
    digit_string = str(input("数字を入力して下さい。"))
    #digit_string = str(an_integer)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)

    if (len(digit_list) != 3):
        print("無効な数字が入力されました。")
        print("三桁の数字を入力してください。")
        main()

    elif (digit_list[0] == digit_list[1] or digit_list[1] == digit_list[2] or digit_list[2] == digit_list[0]):
        print("無効な数字が入力されました。")
        print("それぞれの桁が違う数字を入力してください。")
        main()
        
    print(" ")
    
    numeron(digit_list,number)
    
def initial():
    
    print("'Numeron 3'へようこそ！")
    print("このゲームは三桁の数字を推測するゲームです。")
    print("最初に三桁の数字を入力してください。")
    print("数字に応じてヒントを返すので、正しい数字を推測してください。")
    print("Enjoy the game!")
    print(" ")
    print("準備はいいですか？")

    main()
        

initial()
    
    

