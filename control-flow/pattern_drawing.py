# A script that uses nested loops to print a square pattern pased on as positive integer

integer = int(input("Enter the size of the pattern:"))
row = 0
while row < integer:
    for i in range(integer):
        print("*", end="")
    print()
    row += 1