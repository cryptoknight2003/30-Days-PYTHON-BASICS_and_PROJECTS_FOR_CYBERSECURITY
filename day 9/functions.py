"""def add_numbers(num1, num2):
    result = num1 + num2

    return result


sum_result = add_numbers(5,  3)
print(sum_result) """


def yeahman():
    print("Yeah MAn i got late ")


yeahman()

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)
