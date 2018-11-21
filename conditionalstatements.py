#conditional statement is used to evaluate a condition.

# if statement ----- if <condition> then <do this>

# if <expr>:
#   <statement>
#   <statememt>
# This is not in the if statement

# if <expr> {<statement>} Used by other languages

# magicNumber = 7

# # the value entered by the user returns as a string
# userNumber = int(input('Please choose a number(0…9) '))
# print ('Your number is ' + str(userNumber))

# # conditional state to compare the user number with the magic number
# # Beware of using = to ==
# typeofmagicnumber = type(magicNumber) # of value type you can't print type
# typeofusernumber = type(userNumber)   # you can only print string
# print("magicNumber " + str(typeofmagicnumber))
# print("userNumber " + str(typeofusernumber))

# if userNumber == magicNumber:
#     print("\tYou guessed right! ")
#     print("\tYou are good at this.")
# else:
#     print("\tYou chose poorly.")
#     print("\tThe number was " + str(magicNumber))

# print("End of program")

namePerson = "Scott"
if namePerson != "Scott": # Name of person is NOT Scott
    print("The person is not Scott")
else: # The person's name IS Scott
    print("The person's name is Scott")

myNumber = 34
if myNumber < 50:
    print("Less than 50")

if myNumber > 50:
    print("Greater than 50")

if myNumber >= 34:
    print("Greater than or equal to 34")

if myNumber <= 34:
    print("Less than or equal to 34")

carKeysOnPerson = True
batteryLevel = 12

# conditional statement to determin if car starts
if carKeysOnPerson and batteryLevel > 11:
    print('start the car')
else:
    print("Car won't start")
    