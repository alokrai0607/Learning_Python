# sort in increaseing order
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in  range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubblesort(arr)
print(arr)

#sort in decreaseing order

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [5,8,1,6,9,7,2,55]
bubble_sort(arr)
print(arr)