def draw_star(x, y, n):
    if (x // n) % 3 == 1 and (y // n) % 3 == 1:
        print(end=" ")
    else:
        if n == 1:
            print("*", end="")
        else:
            draw_star(x, y, n // 3)


n = int(input())

for x in range(n):
    for y in range(n):
        draw_star(x, y, n)
    print()
