print("Welcome to the Interactive Personal Data Collector!")

print()

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favourite number: "))

print()

print("Thank you! Here is the information we collected: ")

print()

print("Name:",name, ("Type:",type(name), "Memory Address:",id(name)))
print("Age:",age, ("Type:",type(age), "Memory Address:)",id(age)))
print("Height:",height, ("Type:",type(height), "Memory Address:)",id(height)))
print("Favourite Number:",fav_num, ("Type:",type(fav_num), "Memory Address:)",id(fav_num)))

print()

boy = print("Your birth year is approximately:",2025-age, "( based on your age of",age,")")

print()

print("Thank you for using the Personal Data Collector. Goodbye!")




