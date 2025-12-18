def common_ele(list1,list2):
    common=[]
    for i in list1:
        if i in list2 and not i in common:
            common.append(i)
    return common
list1=list(map(int,input("Enter a list1: ").split()))
list2=list(map(int,input("Enter a list2: ").split()))
print("COmmon elements are: ",common_ele(list1,list2))