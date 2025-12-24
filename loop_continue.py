# Infinite loop that keeps asking the user if they want to continue
while True:
    # Ask the user for input
    answer = input("Do you want to continue? (y/n): ")

    # If the user chooses 'n', exit the loop
    if answer == "n":
        break

    # This message is shown if the loop continues
    print("Program is running again")

# This line is executed after the loop ends
print("Program stopped")
