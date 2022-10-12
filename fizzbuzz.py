# Core:
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number For numbers which are multiples of both three and five
# print "FizzBuzz".

num = 1

while num <= 100:
    if num % 15 == 0:
        print("FizzBuzz")  # Multiple of 15, displays "FizzBuzz"
    elif num % 3 == 0:
        print("Fizz")  # Multiple of 3, displays "Fizz"
    elif num % 5 == 0:
        print("Buzz")  # Multiple of 5, displays "Buzz"
    else:
        print(num)
    num += 1  # Incrementing the number, else infinite loop

