st=input("Enter a string ")
vowels=constant=digits=special_character=0

for i in st:
    if i in "aeiouAEIOU":
        vowels+=1
    elif i.isdigit():
        digits+=1
    else:
        special_character+=1

print("vowels: ",vowels, "digits: ",digits,"special character: ",special_character)
