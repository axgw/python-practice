# Fizz Buzz - Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.


def fizz_buzz(n: int):
    result = ""
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            result += "FizzBuzz\n"
        elif n % 3 == 0:
            result += "Fizz\n"
        elif n % 5 == 0:
            result += "Buzz\n"
        else:
            result += f"{str(n)}\n"
    return result


print(fizz_buzz(100))