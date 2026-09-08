# Use the math library to compute the hypotenuse of a right triangle using the Pythagorean Theorem: c = sqrt(a^2 + b^2)
import math

# Ask the user to enter the lengths of sides A and B
A = float(input("Enter the length of side A: "))
B = float(input("Enter the length of side B: "))

# Compute the hypotenuse using sqrt() and pow()
Squared = math.pow(A,2) + math.pow(B,2)
C = math.sqrt(Squared)

# Display the result
print("The hypotenuse of the right triangle is {:.2f}".format(C))
