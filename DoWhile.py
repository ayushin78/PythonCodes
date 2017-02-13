# while True:
#
#     try:
#         number=int(input('Please Enter a number: '))
#         break
#
#     except ValueError:
#         print("You did not enter a number")
#
#     except:
#         print("An unknown error occured")
#
#
# print("Thank you for entering a number")
secret_number=7
while True:

    try:
        guess_number = int(input("Guess a number between 1 and 10"))


    except ValueError:
        print("you did not enter a number")
        continue

    if(guess_number!=secret_number):
        print("tyou guessed a wrong number")

    else:
        print("you guessed correctly")
        break


