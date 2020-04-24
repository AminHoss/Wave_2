column, row = input("Please enter the coordinates of your square: ")
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
#This might need some explanation, 
column_parity = (letter_list.index(column)+ 1) % 2
row_parity = int(row) % 2
if column_parity == row_parity:
    print("The square is black")
else:
    print("The square is white")
