# Requirements
#   Convert length (standard and metric)
#   Convert volume (standard and metric)
#   Convert temperature (Celsius and Fahrenheit)

# Scope Creep
#       Cool if the program had a GUI

# Refactoring 
#       Make improvements to the code
#       How to make the code more efficient
#       DRY --> Don't Repeat Yourself

# Pseudo-code -- In our own words --> figuring out the logic of the program ---> Comments

# User input as to which conversion they want to do

while True:
    # Ask user
    userChoice = input('Please select: \n'
                            '\t1. Inches to Millimeters \n'
                            '\t2. Millimeters to Inches \n'
                            '\tQ. Quit\n') # If the user types 'quit' -- Do the same thing as 'Q'

    userChoice = userChoice.upper()

    # Create a conditional statement
    if userChoice == '1':
        # Convert inches into millimeters

        # Get information from the user
        userInches = input('Please specify inches: ') # this returns type str

        # Perform the conversion
        # 1 inches = 25.4 mm
        outputMM = float(userInches) * 25.4

        # Output the results to the user.
        # EX 1 in --> The length of 1 in. is equal to 25.4 mmprint(outputMM)
        print('The length of ' + userInches + 'in. is equal to ' + str(outputMM) + 'mm')

    elif userChoice == '2':
        # Convert millimeters into inches

        # Get information from the user
        userMillimeters = input('Please specify millimeters: ') # values as string

        # Perform the conversion
        # 1 millimeter = 0.0393701
        outputIn = float(userMillimeters) / 25.4

        # Output the results to the user.
        # EX 1 mm --> The length of 1 mm is equal to 0.0393701 millimeters
        print('The length of ' + userMillimeters + 'mm. is equal to ' +str(outputIn) + 'In.')
    elif userChoice == 'Q' or userChoice == 'QUIT': # Line 25 already made the input all caps, so Quit, quit, quiT will come here as QUIT
        break
    else:
        # This is anything that is not 1 or 2
        print('that is not an option')