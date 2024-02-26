def Bubblesort(a):
    n=len(a)
    for i in range(n-2):
        for j in range(n-2-i):
            if a[j]>a[j+1]:
                temp=a[i]
                a[i]=a[j+1]
                a[j+1]=temp
x=[]
s=int(input("Enter the size of the array:"))
while True:
    if len(x)<s:
        arr=int(input("Enter the array elements:"))
        x.append(arr)
    else:
        break
print("before sorting:",x)
Bubblesort(x)
print("After sorting:",x)
