import copy
list=[[1,2,3],[4,5,6],[7,8,9]]
shallow = list.copy()
deep = copy.deepcopy(list)

list[0][0]=99
print("original list:", list)
print("shallow copy: ", shallow)
print("deep copy: ", deep)
