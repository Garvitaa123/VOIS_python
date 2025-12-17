list=[1,2,4,1,1,2,5,6,3,5,1,7,4]
new_list=[]

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)