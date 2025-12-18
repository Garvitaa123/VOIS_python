import nums


def avg_num(*args):
    sum=0
    count=0
    for num in args:
        sum+=num
        count+=1
    return sum/count
nums=list(map(int,input("Enter a list: ").split()))
print("average is: ",avg_num(*nums))