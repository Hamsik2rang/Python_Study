# Boyer-Moore majority vote algorithm

numbers = [1, 3, 2, 5, 3, 3, 1, 3, 4, 3]
count = 0

for i in numbers:
    # count가 0이면 새로운 원소를 후보로 지정한 후 count를 1로 설정
    if count == 0:
        candidate = i
        count = 1
    # 이번에 읽은 원소가 후보와 동일한 값을 가지는 경우 count 1 증가, 그렇지 않으면 1 감소
    count += (candidate == i) and 1 or -1

if count > 0:
    print(f"Major number is {candidate}")
else:
    print(f"None of major number")