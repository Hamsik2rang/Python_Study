# Raise Exception if string inputted is not Pelindrome.
class StringNotPelindromeError(Exception):
    def __init__(self):
        super().__init__("It's not pelindrome.")


def is_pelindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_pelindrome(s[1:-1])


s = input("Type String: ")
try:
    if not is_pelindrome(s):
        raise StringNotPelindromeError
except Exception as e:
    print(e)
else:
    print(f"{s} is Pelindrome.")
finally:
    print("Check Finished.")