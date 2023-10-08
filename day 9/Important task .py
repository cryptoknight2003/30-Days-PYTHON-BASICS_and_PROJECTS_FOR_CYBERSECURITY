# Create a program that can take in input of the users name
# save the name in a variable
# pass the variable through and function and print "Hello_____"

user_name = input("What is your name ?")

def function(user_name):
    print(f"Hello{user_name}")

function(user_name)