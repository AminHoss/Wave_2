from math import sqrt
a = float(input("Enter the value for a:"))
b = float(input("Enter the value for b:"))
c = float(input("Enter the value for c:"))

discrimant = (b * b) - (4 * a * c)

if discrimant < 0:
    print("There are no real roots to this equation")
elif discrimant == 0:
    print("There is only one real root to this equation")
elif discrimant > 0:
    print("There are two real roots to this equation")

if discrimant == 0:
    answer =  (0 - b) / (2 * a)
    print("The root of the equation is {}.".format(answer))
elif discrimant > 0: 
    answer_a = (-b + sqrt( (b * b) - (4 * a * c) )) / (2 * a)
    answer_b = (-b - sqrt( (b * b) - (4 * a * c) )) / (2 * a)
    print("The roots of the equation are {} and {}.".format(answer_a, answer_b))
