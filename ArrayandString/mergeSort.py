def mergeSort(num,m,num1,n):
    num[m:]=num1
    num.sort()
    return num

num=[1,2,3,0,0,0]
m=2
num1=[2,5,6]
n=3
print(mergeSort(num,m,num1,n))