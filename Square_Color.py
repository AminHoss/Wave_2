column, row = input("Please enter the coordinates of your square: ")
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
column_parity = (letter_list.index(column)+ 1) % 2
#The reason there is a +1 for the index function is because the list starts at 0, so the 1st row would be counted as an even row, 
#while it is an odd row, so the +1 fixes this problem.
row_parity = int(row) % 2
if column_parity == row_parity:
    print("The square is black")
else:
    print("The square is white")
