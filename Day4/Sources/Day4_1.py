# global scope는 C의 전역 변수처럼 예상치 못하게 값을 수정할 가능성이 존재하니 웬만하면 쓰지 말자.

enemies = 1


def increse_enemies():
    global enemies
    enemies = 3
    print(enemies)


increse_enemies()
print(enemies)

# 다른 scope라 해도, 값을 수정하는 것이 아니라면 사용할 수 있다.

PI = 3.141592


def get_circle_area(radius):
    area = (radius ** 2) * PI
    return area


print(f"if radius is {2}, area is {get_circle_area(2):.4}.")
