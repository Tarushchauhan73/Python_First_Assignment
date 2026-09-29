
cities = ("Delhi", "Mumbai", "Chandigarh", "Bangalore", "Pune")


print("First city:", cities[0])


print("Last city:", cities[-1])


print("Length of tuple:", len(cities))


city = input("Enter a city to search: ")


if city in cities:
    print("City exists in the tuple.")
else:
    print("City does not exist in the tuple.")