month = input("Please enter the month (in capital letters): ")
thirty_one_days = ["January", "March", "July", "August", "October", "December"]
thirty_days = ["April", "June", "September", "November"]
twenty_nine_days = ["February"]
if month in thirty_one_days:
    print("{} has 31 days".format(month))
elif month in thirty_days:
    print("{} has 30 days".format(month))
elif month == "February":
    print("{} has 28 or 29 days".format(month)) 
else:
    print("Our program has not been able to recognize the month entered. Please try again.")
