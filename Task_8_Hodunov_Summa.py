def fact(n):
    if n != 1:
        return n[0]
    return n * fact(n - 1)

print(fact(5349))