# sum of even numbers in 1 to 100

even_sum = 0
for i in range(1, 101):  # or for i in range(2,101,2):
    if i & 1 == 0:
        even_sum += i

print(even_sum)
