# for i in range(10):
#     if i % 2 ==0:
#         continue
#     print(i)


# for i in range(10):
#     if i == 5 :
#         break
#     print(i)

# count = 5
# while count > 0:
#     print(count)
#     count -= 1


# loop through a list
# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

# Syntax for for-loop
# for item in sequence:
#     #code


# #Ex1
# num = 10
# if num > 0 :
#     print("Positive number")
# elif num == 0 :
#     print("Zero")
# else:
#     print("Negative Number")
# #Ex2 Nested condition
# age = 25

# if age > 18:
#     if age < 30:
#         print("Young Adult")
#     else:
#         print("Adult")
#####################################################
## Exercise 1: Check if a Number is Prime
# user_input = int(input())
# try:
#     if user_input > 1:
#         for i in range(2,user_input):
#             if user_input % i == 0:
#                 print("Not prime")
#                 break
#         else:
#             print("Prime")
#     else:
#         print(f"{user_input} is not a Prime")

# except:
#     print("Not Valid")
###Exercise 2
# const =True
# while const:
#     print("This is The best calculator")
#     print("choose 1 for submission")
#     print("choose 2 for Multification")
#     print("choose 3 for sumation")
#     print("choose 4 to exit")
#     choice = int(input())
#     try:
#         if choice == 1:
#             print("Enter two numbers")
#             print("number 1:")
#             num1 = float(input())
#             print("number 2:")
#             num2 = float(input())
#             print(num1 - num2)
#         elif choice == 2:
#             print("Enter two numbers")
#             print("number 1:")
#             num1 = float(input())
#             print("number 2:")
#             num2 = float(input())
#             print(num1 * num2)
#         elif choice == 3:
#             print("Enter two numbers")
#             print("number 1:")
#             num1 = float(input())
#             print("number 2:")
#             num2 = float(input())
#             print(num1 + num2)
#         elif choice == 4:
#             break
#     except:
#         print("Not valid number")
########################################################
# def factorial(num:int):
#     num2 = 1
#     for i in range(1, num+1):
#         print(i)
#         num2 = num2 * i
#     return num2
# print(factorial(22))
#############################################