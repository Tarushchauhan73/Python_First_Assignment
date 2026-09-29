marks = [80, 75, 90, 85, 70]


total = 0

for mark in marks:
    total = total + mark


average = total / len(marks)


print("Total marks:", total)
print("Average marks:", average)
print("Highest mark:", max(marks))