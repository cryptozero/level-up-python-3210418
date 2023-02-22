def get_prime_factors(n):
    result = []

    i = 2

    while i <= n:
        if n % i == 0:
            result.append(i)
            n = n // i
        else:
            i += 1
    if not result:
        result = [1]
    return result


if __name__ == "main":
    assert get_prime_factors(630) == [2, 3, 3, 5, 7]
    assert get_prime_factors(1) == [1]
    assert get_prime_factors(13) == [13]
