from typing import List

# introduce
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True

# fixture
def load_numbers_sorted(txt: str) -> List[int]:
    numbers = []

    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))

    return numbers


# capsys out
def fibonacci(n: int):
    a = 0
    b = 1

    for _ in range(n):
        print(b)

        a, b = b, a + b