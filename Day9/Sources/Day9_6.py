# dictionary comprehension

d = ["a", "b", "c", "d"]
a = {key: value for key, value in dict.fromkeys(d).items()}

print(a)

b = {key: value for key, value in {"a": 1, "b": 2, "c": 3}.items()}
print(b)

x = {
    "a": 3,
    "b": 5,
    "c": 4.4,
}

c = {key: value for key, value in x.items() if not isinstance(value, float)}
