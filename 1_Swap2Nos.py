#n1 = 10
#n2 = 20

n1 = input('Enter number 1: ')
n2 = input('Enter number 2: ')
print('value of number 1 before swapping:', n1)
print('value of number 2 before swapping:', n2)

#Approach 1 using temporary variables
#temp = n1;
#n1 = n2;
#n2 = temp;

# Approach 2 without using temp variable
n1,n2 = n2,n1

print('value of number 1 after swapping:', n1)
print('value of number 2 after swapping:', n2)



