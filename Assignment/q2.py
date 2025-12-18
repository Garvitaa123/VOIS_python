def char_count(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
s=input("Enter a string")
print("character_count: ",char_count(s))