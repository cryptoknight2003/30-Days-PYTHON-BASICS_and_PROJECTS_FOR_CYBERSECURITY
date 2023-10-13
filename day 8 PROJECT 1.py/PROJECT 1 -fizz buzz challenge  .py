# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz



def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function with the desired range (e.g., 100 for numbers 1 to 100)
fizz_buzz(100)
Explanation:

   ''' We define a function fizz_buzz that takes a single argument n, which represents the range of numbers to be checked (from 1 to n).

    We use a for loop to iterate through numbers from 1 to n, inclusive.

    Inside the loop, we use if statements to check if the current number is a multiple of 3 and/or 5. We start with the most specific condition (multiples of both 3 and 5) and work our way down to the least specific conditions.

    If the current number is a multiple of both 3 and 5, we print "FizzBuzz." If it's only a multiple of 3, we print "Fizz." If it's only a multiple of 5, we print "Buzz." If it's not a multiple of either 3 or 5, we print the number itself.

    The fizz_buzz function is called with the desired range (e.g., fizz_buzz(100) will print FizzBuzz for numbers from 1 to 100).

This code provides an efficient and straightforward solution to the FizzBuzz problem, with clear and concise logic for checking divisibility by 3 and 5. '''


# else code taught by PhD security and my brain


''' for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num) ''' 
