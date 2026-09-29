a = {5, 10, 15, 20, 25, 30}
b = {30, 35, 40, 45, 50, 55}

print("union of two sets is:", a | b)
print("intersection of two sets is:", set(a & b))
print("difference of two sets is:", set(a - b))
print("common elements in two sets are:", set(set(a) & set(b)))
