def arrIntergerCount(ar, x):
    count = 0
    for i in ar:
        if (i == x):
            count = count + 1
    return count



# Driver Code
arr = [2,3,4,3,2,1]
x = 3
value = arrIntergerCount(arr, x)
print('{} has occurred {} times'.format(x, value))