# Create the number to be guessed
intAns = 12345

# Get input from user
intGuess = int(input("Enter Number: "))

# Print users guess to the screen for validation
print("Your guess = ", intGuess)

# main testing sequence
if intGuess == intAns:
    print("is Correct")
else:
    print("is Wrong")
