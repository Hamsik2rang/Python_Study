def is_pelindrome(word):
    if len(word)<2:
        return True
    elif word[0]!=word[-1]:
        return False
    return is_pelindrome(word[1:-1])


word = input("Type word to check it is pelindrome: ")
print(is_pelindrome(word))
