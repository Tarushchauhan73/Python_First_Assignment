userinput = int(input("Enter a year: "))

if (userinput % 4 == 0 and userinput % 100 != 0) or (userinput % 400 == 0):
    print(userinput, "is a leap year.")
else:
    print(userinput, "is not a leap year.")     