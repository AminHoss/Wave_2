import random
numbers = [0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32, 34, 36]
black= [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31, 33, 35]

number = random.choice(numbers)
print(number)
if number == 0:
    print("Pay 0")
elif number == 00:
    print("Pay 00")
else:
    if number in red:
        print("Pay Red")
    elif number in black:
        print("pay Black")
    if number % 2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")
    if number in range(1, 19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")
