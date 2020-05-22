# Input [2,5,7,9]
# Out [9,5,7,2]

#Approach 1  --> temporary variable

mylist = [2,5,7,9,85,45,74]
size = len(mylist)
temp = mylist[0]
mylist[0] = mylist[size-1]
mylist[size-1] = temp
print("Swapped list approach 1: ", mylist)

#Approach 2 -->
mylist = [2,5,7,9,85,45,74]
mylist[0],mylist[-1] = mylist[-1],mylist[0]
print("Swapped list approach 2: ", mylist)

#Approach 3 -- > by using tuple variable
mylist = [2,5,7,9,85,45,74]
get = (mylist[-1],mylist[0])  #Packing
mylist[0],mylist[-1] = get
print("Swapped list approach 3: ", mylist)

# Approach 4 -- > Using * operand
mylist = [2,5,7,9,85,45,74]
start,*middle,end = mylist
mylist = end,*middle,start
print("Swapped list approach 4: ", mylist)

# Approach 5 -- > Using pop buildin function
mylist = [2,5,7,9,85,45,74]
first = mylist.pop(0)
last = mylist.pop(-1)

mylist.insert(0,last)
mylist.append(first)
print("Swapped list approach 5: ", mylist)