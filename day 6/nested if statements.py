score = input("Enter your score out of 100")
score = int(score)

if score >= 90:
    age = int(input("what is your age ?  "))
    if age < 10:
        print("congratulations you got : GRADE A+")
    else:
        print("your grade is A")
elif score >= 80:
    age = int(input("what is your age ?  "))
    if age < 18:
        print("congratulations you got : GRADE B+")
    else:
        print("your grade is B")

elif score >= 70:
    age = int(input("what is your age ?  "))
    if age < 25:
        print("congratulations you got : GRADE c+")
    else:
        print("your grade is c")

elif score >= 60:
    age = int(input("what is your age ?  "))
    if age < 30:
        print("congratulations you got : GRADE D+")
    else:
        print("your grade is D")

elif score < 60:
    print("Yo nigga you gotta improve yourself ")

# it was a bit of a trouble for me to do it on my own, but I tried my best to do it
