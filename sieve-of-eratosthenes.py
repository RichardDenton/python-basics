import math
def primes(limit):
    """
    limit: an integer
    returns: a list of all prime numbers up to the limit
    """
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False
    for n in range(int(math.sqrt(len(numbers))) + 1):
        if numbers[n]:
            for k in range(n ** 2, limit + 1, n):
                numbers[k] = False
    return [x for (x, y) in enumerate(numbers) if y]
