def answer(n):
    answer = (2 * (n ** 2) + 2 ** n) / 10e-9
    return answer


print(answer(10))
print(answer(20))
print(answer(50))
print(answer(100))