# Lambda function

def plus(a,b):
    return a + b

res = plus(5,10)
print(res)

res = lambda a, b: a+b
print(res(5,10))

print((lambda a,b: a+b)(5,10))