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

# 22-oct-24 11:10 AM 

# ------------ Q7 Write a program to print the Pascal’s triangle.

'''

def fact(n):
    if n == 0:
        return 1
    else:
        i, prod = 1, 1
        while i <= n:
    
            prod *= i
            i += 1
        return prod

n = int(input("Enter the number of rows: "))

for i in range(0, n):
    for j in range(0, i+1):
        o_p = (fact(i)) // (fact(i-j) * fact(j))
        print(o_p, end = " ")
    print()


'''

# ------------ Q8 Write a program to check if a year is a leap year.

'''

year = int(input("Enter the year to be checked: "))

if (year % 4) == 0 and (year % 100) != 0: 
    print("Leap year")
elif (year % 100) == 0 and (year % 400) == 0: 
    print("Leap year")
else:
    print("Not a Leap year")

'''

# ------------ Q9 Write a program to print the sum of even and odd numbers in a given range.

'''

lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

sum_even, sum_odd = 0, 0

for i in range(lower_bound, upper_bound+1):
    if (i % 2) == 0:
        sum_even += i
    else:
        sum_odd += i

print("Sum of even numbers is: ", sum_even)
print("Sum of odd numbers is: ", sum_odd)

'''

# ------------ Q10 Write a program to print a pyramid pattern using stars.

'''
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = " ")       # end = " " to print on the same line
    print()                         # to print on next line after one row ends

'''
