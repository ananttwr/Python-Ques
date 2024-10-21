# 21-oct-24 5:12 PM 
# Loops and Control Structures

# ------------ Q1 Write a program to print a multiplication table for a given number.

'''

number = int(input("Enter the number: "))

for i in range(1, 11):
    print(number, "*", i, "=", number*i)

'''

# ------------ Q2 Write a program to print the sum of all numbers in a range provided by the user.

'''

number1 = int(input("Enter the lower bound: "))
number2 = int(input("Enter the upper bound: "))
sum = 0

for i in range(number1, number2+1):
    sum += i
    
print(sum)

'''

# ------------ Q3 Write a program to reverse a given number.

'''

number = int(input("Enter the number: "))
rev, last = 0, 0

while number != 0:
    last = number % 10
    rev = (rev * 10) + last
    number = number // 10               # integer divison

# print("reverse of the number", number, "is", rev)
print(rev)

'''

# ------------ Q4 Write a program to check if a number is an Armstrong number.

'''

number = input("Enter the number: ")

ran = len(number)
sum = 0

for i in range(0, ran):
    sum += int(number[i]) ** 3

if int(number) == sum:
    print("Armstrong number")

else:
    print("Not an Armstrong number")

'''

# ------------ Q5 Write a program to find the sum of digits of a number.

'''

number = input("Enter the number: ")

ran = len(number)
sum = 0

for i in range(0, ran):
    sum += int(number[i])

print(sum)

'''


# ------------ Q6 Write a program to print the first n prime numbers.

'''

number = int(input("Enter the number: "))

for i in range(2, number+1):
    flag = True

    for j in range(2, i):
        if (i % j) == 0:
            flag = False
            break

    if (flag == True):
        print(i)
    
'''

# ------------ Q7 Write a program to print the Pascal’s triangle.

'''
def fact(n):
    i, prod = 1, 1
    while i != n:

        prod *= i
        i += 1
    return prod

n = int(input())
r = n
for i in range(0, n):
    for j in range(0, n):

        print((fact(n)) / (fact(n-r) * fact(r)))

'''
