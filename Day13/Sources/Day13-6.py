# Bottom up Fibonacci in Python

fibo = [1, 1]

for _ in range(8):
    fibo = [fibo[-1], fibo[-1]+fibo[-2]]
    
print(fibo[-1])