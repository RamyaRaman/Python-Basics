# 5 = 1*2*3*4*5

#Approach 2 - recursive

def factorial(n):
    # if(n==0 or n==1):
    #     return 1
    # else:
    #     return n * factorial(n-1)
    # Ternary operator
    return 1 if(n==0 or n==1) else n * factorial(n-1)

num = int(input("Enter number"))
print("Factorial of",num,"is",factorial(num))