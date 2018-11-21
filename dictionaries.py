# Dictionary is a type of list
# Uses a Key --> value pair
# Example
#    Key    -->    Value
# W08675309 --> John Wildcat
# W02030040 --> Jane Wildcat

students = {
    "firstName" : "Scott", 
    "lastName"  : "Hadzik", 
    "W#"        : "W234",
    "email"     : "scotthadzik@weber.edu"
}

bestStudent = students["firstName"]
print (bestStudent)

print (students)
students["firstName"] = "Jill"
print (students)