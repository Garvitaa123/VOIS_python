s="hello"
try:
    s[0]='J'
except TypeError:
    print("Strings are immutable")
