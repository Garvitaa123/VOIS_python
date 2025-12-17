st=input("Enter a string ")

words=st.split()
result=[]

for word in words:
    print(word[::-1],end=" ")