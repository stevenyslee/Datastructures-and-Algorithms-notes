#
# Given an array of size n that contains elements 1->n-1, find the duplicate
#
#
from random import randint


# Allows for constant space on O(n) speed
# Solution derives from Sum of numbers from 1 to n (not included) which equals to n*(n-1)/2,
# subtracting the 2 results, gives us the extra number

def find_through_sum(a: list):

    l_sum = 0
    for x in a:
        l_sum += x

    n = len(a)
    series_sum = (n) * (n - 1) / 2

    return l_sum - series_sum

# O(n) speed with o(n) space
def hash_solution(a: list):
    u = dict()
    for x in a:
        if x in u:
            return x
        else:
            u[x] = True


# Iterate over all elements once and then over (n-1) expected elements, the remaining element will stay as it will be xor'd 3 times
# X^X = 0, X^X^X = X, X^A^X^A^A = X^A^X = A
def xor_solution(a: list):
    xor = 0
    for x in a:
        xor ^= x
    for x in range(1, len(a)):
        xor ^= x
    return xor


l = [x for x in range(1, randint(5, 20))]
l.append(randint(1, randint(1, 20)))

print(l)
print(find_through_sum(l))
print(hash_solution(l))
print(xor_solution(l))
