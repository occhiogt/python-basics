# Ask the user for their age and convert the input to an integer
age = int(input("How old are you? "))

# Check the age and determine the correct category
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")
