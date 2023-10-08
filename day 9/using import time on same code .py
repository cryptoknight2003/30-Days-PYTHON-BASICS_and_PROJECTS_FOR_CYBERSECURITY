import time
choice = int(input("What number would you like to choose ?"))
def functiion(choice):
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")

        elif num % 3 == 0:
            print("Fizz")

        elif num % 5 == 0:
            print("Buzz")

        else:
            print(num)
print("Your code will boom shortly")
time.sleep(3)
functiion(choice)