import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
def insertionsort(a):
    n=len(a)
    for i in range(1,n):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
            print(a)
a=[]
size=int(input("enter the size of array:"))
while True:
    if len(a)<size:
        arr=int(input("enter the array elements:"))
        a.append(arr)
    else:
        break
print("Before sorting:",a)
insertionsort(a)
print("After sorting:",a)
x=list(range(1,100))
plt.plot(x,[y*y for y in x])
plt.title("Insertion sort - Time complexity is O(n\u00b2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
