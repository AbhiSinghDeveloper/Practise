arr=[2,7,11,15]
target=9
a=len(arr)
def sum(arr,target):
    for i in range(0,a):
        for j in range(i,a):
            if(arr[i]+arr[j]==target):
               print(arr[i],arr[j])
               return i,j
print(sum(arr,target))
