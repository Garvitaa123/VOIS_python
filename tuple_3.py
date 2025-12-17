t=tuple(map(int,input("Enter tuple elements").split()))
x=int(input("enter the element to count"))
count=0
for i in t:
    if i==x:
        count+=1
print(count)