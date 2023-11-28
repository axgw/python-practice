# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes
# to reach one using the following process: If n is even, divide it by 2. If n is odd,
# multiply it by 3 and add 1.

def collatz(n: int):
    count = 0
    while n > 1:
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        count += 1
    return count
