# A script that calculates the multiple of any given number from 1-10 using for loops                                                                                                                                                                                                                                                                       

# Prompting the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# A for loop to calculate and print the multiplication table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
