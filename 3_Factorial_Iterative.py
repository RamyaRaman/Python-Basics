# 5 = 1*2*3*4*5

#Approach 1 - iterative
fact = 1
num = int(input('Enter number '))

if num < 0:
    print("Factorial doesn't exist")
elif num == 0:
    print("Fact of zero is 1")
else:
    for i in range(1,num+1):
        fact = fact * i
    print("Factorial of", num, "is", fact)
