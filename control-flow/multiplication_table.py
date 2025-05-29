# A script that calculates the multiple of any given number from 1-10 using for loops                                                                                                                                                                                                                                                                       

# Prompting the user for a number
number = int(input("Enter a number to see its multiplication table: "))
# Declaring an array for multiples 1-10
multiple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A for loop to calculate and print the multiplication table
for item in multiple:
    print(f"{number} * {item} = {number * item}")
