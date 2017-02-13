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
# secret_number=7
# while True:
#
#     try:
#         guess_number = int(input("Guess a number between 1 and 10"))
#
#
#     except ValueError:
#         print("you did not enter a number")
#         continue
#
#     if(guess_number!=secret_number):
#         print("tyou guessed a wrong number")
#
#     else:
#         print("you guessed correctly")
#         break

# from decimal import Decimal as D
#
# sum = D(0)
#
# sum += D('0.1')
# sum += D('0.1')
#
# sum -= D('0.2')
#
# print('sum = ', sum)
#
# print('0.1 + 0.1 - 0.2 = ', 0.1 + 0.1 + .1 - .3)
#
# print(type(3))
# print(type(3.14))
# print(type("3"))
# print(type('3'))
# samp_string = "Hello! This is very interesting"
# print(samp_string[0:4]) #slicing of string
# print(samp_string[4:])
#
# print("Hello " * 5)
#
# print(type(str(4)))
#
# for char in samp_string:
#     print(char)
#
# for i in range(0, len(samp_string)-1, 2):
#     print(samp_string[i]+samp_string[i+1])


while True:
    try:
        msg = input('Enter a string in uppercase : ')
        secret_msg = ""
        for i in range(0, len(msg)):
            secret_msg += str(ord(msg[i]))

        print("Secret message : "+secret_msg)

        original_number=""
        for i in range(0, len(secret_msg)-1, 2):
            original_number += chr(int(secret_msg[i] + secret_msg[i+1]))

        print("Original String : " + original_number)

        break

    except ValueError:
        print("please enter a valid string")






