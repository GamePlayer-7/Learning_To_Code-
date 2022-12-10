import calendar

yy = int(input("Enter year: "))         # To take year input from the user
mm = int(input("Enter month: "))        # To take month input from the user

print(calendar.month(yy, mm))           # To display calendar

# Below is the Output :

Enter year: 2022
Enter month: 12
   December 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
