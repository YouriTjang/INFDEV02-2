

def rec_fact(n):
    if n <= 1:
        return 1
    else:
        return n * rec_fact(n-1)
print(rec_fact(6))


def it_fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(it_fact(6))