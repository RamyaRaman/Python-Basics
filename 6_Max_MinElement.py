#Input : arr[] = {10 20 4}
#Output : 20 and 4

#Finind max element
arr = [40,20,3,4,5]
max = arr[0]
n = len(arr)
for i in range(1,n):
    if arr[i] > max:
        max = arr[i]

print("Maximum element is ", max)

#Finind min element
arr = [40,20,3,4,5]
min = arr[0]
n = len(arr)
for i in range(1,n):
    if arr[i] < min:
        min = arr[i]

print("Minimum element is ", min)