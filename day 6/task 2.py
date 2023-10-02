# Write a program that prompts the user to enter their score (out of 100) and
# displays their corresponding grade based on the following criteria :
#
# Scores 90 and above : Grade A
# scores 80 to 89 : Grade b
# scores 70 to 79 : Grade c
# scores 60 to 69 : grade d
# scores below 60 : grade f
score = input("Enter your score out of 100")
score = int(score)

if score >= 90:
    print("congratulations you got : GRADE A")


elif score >= 80:
    print("congratulations you got : GRADE B")

elif score >= 70:
    print("congratulations you got : GRADE C")

elif score >= 60:
    print("congratulations you got : GRADE D")

elif score < 60:
    print('Yo nigga you gotta improve yourself !!! You got a fucking grade F')  ###

# it was a bit of a trouble for me to do it on my own, but I tried my best to do it
