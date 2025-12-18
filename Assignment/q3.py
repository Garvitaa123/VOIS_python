num=int(input("Enter a number: "))
def is_palindrome(num):
    s=str(num)
    if s==s[::-1]:
        print(True)
    else:
        print(False)
print(is_palindrome(num))