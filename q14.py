userinput = int(input("Enter the marks: "))

if userinput >= 90:

    print("Grade: A")
elif userinput >=75 and userinput <=89 :

    print("Grade: B")
elif userinput >=60 and userinput <=74 :

    print("Grade: C")

elif userinput >=40 and userinput <=59 :
    print("Grade: D")
else:
    print("Grade: F")