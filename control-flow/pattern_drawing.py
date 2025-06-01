# pattern_drawing.py

# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to handle columns
    for col in range(size):
        print("*", end="")  
    print()  
    row += 1
