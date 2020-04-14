"""
Takes an iterable of two member iterables as fractions and converts them
to a format to be added, with denominator as least common multiple between
all items.  

This isn't the most efficient, but it is still O(n), although the list needs
to be stepped through twice.  
"""


def convert_fractions(fractions):
    least_com_mul = lcmm(*[fract[1] for fract in fractions])
    results = []

    for fraction in fractions:
        numerator, denominator = fraction
        results.append([
            numerator * (least_com_mul // denominator),
            least_com_mul
        ])

    return results


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)


def lcmm(*args):
    if len(args) == 0:
        return None
    result = args[0]
    for i in range(1, len(args)):
        result = lcm(result, args[i])
    return result



test_a = a = [[1, 2], [1, 3], [1, 4]]

print(convert_fractions(test_a))
