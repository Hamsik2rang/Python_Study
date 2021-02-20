# set comprehension

a = {i for i in "rabbit"}
print(a)

a = {i for i in "rabbit" if ord(i) % ord("a") < 13}
print(a)
