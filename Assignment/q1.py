def even_num(lst):
    result=[]
    for i in lst:
        if i%2==0:
            result.append(i)
    return result
lst=list(map(int,input("Enter a list seperated by space: ").split()))
print(even_num(lst))