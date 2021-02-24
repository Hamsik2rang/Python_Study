# Bottom up Fibonacci in Python

fibo = [1, 1]

for _ in range(8):
    fibo.append(fibo[-2] + fibo[-1])
    
print(fibo)