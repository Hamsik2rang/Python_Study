# 1일차
## 공부한 내용

1.  **파이썬의 기본적인 입출력 방법**
    -   print()
    -   input()

2.  **기본 자료형(Primitive Types)**
    -   string (String Type)
    -   int (Integer Type)
    -   float (Floationg Point Type)
    -   bool (Boolean Type)

3.  **기초 연산자(Operator)**
    -   산술 연산자(Arithmetic Operators)
    -   비교 연산자(Comparison Operator)
    -   논리 연산자(Logical Operators)

4.  **조건문**
    -   if ~ else
    -   if ~ elif ~ else
    -   중첩 조건문(Nested If)
    -   다중 조건문(Multiple If)

----

### 1. 파이썬의 기본적인 입출력 방법

C에서 기본 입출력 함수로 `printf`, `scanf`를 이용하듯이, 파이썬은 `print`, `input `함수를 이용한다.

#### print()

***Reference = print(\*\*objects*, *sep=' '*, *end='\n'*, *file=sys.stdout*, *flush=False*)**

```python
print("output string")
```

print 함수는 기본적으로 String value를 인자로 전달받으므로, 그 외 자료형을 출력하고자 한다면 이를 String type으로 Conversion해야 한다.

Type conversion은 다음과 같이 C++ style 형변환과 동일한 형태로 이루어진다.

```
i = 3
f = 4.4
b = True

str(i)
str(f)
str(b)
```

만약 별도의 형 변환 없이 값을 출력하고자 하는 경우, **F String**을 이용해 전달할 수 있다.

```python
github_name = f"Hamsik{2}rang"
age = 25

print(f"Hello, I'm {age} years old.")
print(f"My height is {182.2421:.1f}cm") #My height is 182.2cm
```

위와 같이 F string은 임의의 string앞에 f를 표기한 후, 문자열 내에 출력하고자 하는 Non-String type의 값을 중괄호로 감싸 전달한다.

#### input()

***Reference = input([*prompt*])***

```python
a = input("a의 값을 입력하세요.")
```

특이하게 매개인자로 프롬프트에 출력할 문자열을 전달할 수 있다.

덕분에 사용자들로 하여금 입력해야 할 값의 안내를 할 때 별도로 출력 함수를 사용하지 않아도 된다.

----

### 2. 기본 자료형(Primitive Types)

파이썬의 기본 자료형은 다음과 같다.

*   **string** (String Type)
*   **int** (Integer Type)
*   **float**(Floating Point Type)
*   **bool** (Boolean Type)

#### String (String Type)

String은 문자열 자료형이며, 타 언어와 같이 "" 로 값을 감싸 표현한다.

다른 언어들과의 차이점이 있다면, "" 외에 ''로도 문자열을 표현할 수 있다는 점이다(다른 언어들은 보통 ''를 문자(Character) 데이터를 표현하기 위해 사용한다).

```python
hello = "Hello\n"
dialog = 'He said, "Hey, I\'m busy!"'
```

문자열은 이름 그대로 문자들의 나열이기 때문에, Index를 이용해 특정 문자에 접근할 수 있다.

```python
print("Hello"[4]) # print 'o'
```

문자열을 구성하는 문자들의 개수를 문자열의 길이라 하며, 이를 파악하기 위해 `len`함수를 이용할 수 있다.

```python
print(str(len("Hello"))) # print "5"
```

#### Int(Integer Type)

Int는 정수 자료형이다.

많은 언어들과 달리 저장할 수 있는 크기의 제한이 존재하지 않기 때문에 미리 데이터의 크기를 가늠하지 않고 편하게 사용할 수 있다.

#### Float(Floating Point Type)

Float는 실수 자료형이다.

파이썬은 실수의 유형에 기본적으로 **배정밀도(Double-Precision)** 를 사용한다.

#### Bool(Boolean Type)

Bool은 논리 자료형이다.

오직 True, False만을 표현하며, 이 때 True, False의 첫 글자를 대문자로 작성해야만 한다.

.

.

.

알아둘 점은, 파이썬의 기본 자료형은 모두 객체이며, 객체 중에서도 **Immutable**한 객체라는 것이다(기본 자료형 외의 Immutable Object는 **Tuple**이 있다).

---

### 3. 기초 연산자(Operator)

#### 산술 연산자(Arithmetic Operator)

파이썬의 산술 연산자는 다음이 있다.

-   **\+** : 덧셈 연산자

-   **\-** : 뺄셈 연산자
-   **\*** : 곱셈 연산자
-   **/** : 나눗셈 연산자
-   **//**: 몫 연산자
-   **%** : 나머지 연산자
-   ****** : 거듭제곱 연산자 
-   **=** : 대입 연산자

```python
a = 3
b = 4

a + b 	# = 7, 		Type is int
a - b 	# = -1, 	Type is int
a * b 	# = 12, 	Type is int
a / b 	# = 0.75, 	Type is float
a // b 	# = 0, 		Type is int
a % b 	# = 3, 		Type is int
a ** b 	# = 81, 	Type is int
a = b	# a is 4
```

보다시피, 나눗셈 연산의 경우 그 결과가 실수 형태로 반환된다(나머지가 0이라 하더라도 실수 형태로 반환됨).

#### 비교 연산자(Comparison Operator)

파이썬의 비교 연산자는 다음과 같다.

-   **==** : Is equal Operator
-   **!=** : Is not Equal Operator
-   **\>** : Is left-Bigger Operator
-   **<** : Is right-Bigger Operator
-   **\>=** : Is left-bigger or equal Operator
-   **<=** : Is right-bigger or equal Operator

비교연산의 결과는 항상 **Bool type value**이다.

#### 논리 연산자(Logical Operator)

파이썬의 논리 연산자는 다음과 같다.

*   **and** : AND Operator, &&
*   **or** : OR Operator, ||
*   **not** : NOT Operator, !

```python
a = True
b = False

if a and b:
	#Not execute
if a or b:
	#Execute
if a and not b:
	#Execute
if not a or b:
	#Not execute
```

