def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n // 2):
            if not n % x:
                return False
        return True
