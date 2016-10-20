# Skeleton code for participant solutions to the squares problem presented
# in workshop. To run the tests for this problem, run the squares_tests.py script
import math

def largest_square(n):
    """Returns the largest perfect square that is smaller than n"""
    return int(math.floor(math.sqrt(n)) ** 2)


cache = {}
def min_square_sum_dyn( n ):
    # Inputs:
    # n: int

    # YOUR CODE HERE. Return an integer representing the minimum number of
    # perfect squares required to sum to n.
    if n <= 0:
        return None
    if n in cache:
        return cache[n]
    else:
        lgst_sq = largest_square(n)
        if lgst_sq == n:
            return 1
        else:
            squares = [i**2 for i in range(1, n) if i**2 <= lgst_sq]
            # print(squares)
            l = [min_square_sum(n - s) for s in squares if s < n]
            cache[n] = 1 + min(l)
            return cache[n]


def min_square_sum(n):
    queue = [(n, 1)]
    while queue:
        current_n, depth = queue.pop(0)
        lgst_sqrt = int(math.sqrt(current_n)) # int floors
        if lgst_sqrt ** 2 == current_n:
            return depth
        queue.extend([(current_n - i**2, depth+1) for i in range(1, lgst_sqrt+1)])

