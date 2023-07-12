def rotate_one(arr):
    n =len(arr)
    last = arr[n-1]
    arr=[last]+arr[0:n-1]
    return arr
arr= list(map(int,input().split()))
k = int(input())
for i in range(k):
    arr=rotate_one(arr)
print(arr)
