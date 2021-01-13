def prime_checker(number):
    i = 2
    while i ** 2 <= number:
        if number % i == 0:
            print(f"{number} is not Prime number.")
            return
    print(f"{number} is Prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

