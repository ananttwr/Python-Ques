# 19-oct-24 9:50 PM 
# Basic Python Programs

# ------------ Q1 Write a program to swap two variables

'''

M1 

first = input("enter first number: ")
second = input("enter second number: ")

new_second = first
new_first = second

print("Number after swapping are: " + new_first + " " + new_second)


M2 without using temp variable

5,10

first = first + second  
5+10 = 15

second = first - second
15-10 = 5

first = first - second
15-5 = 10

'''

# ------------ Q2 Write a program to check if a number is even or odd.

'''

number = int(input("Enter the number to be checked: "))

if number % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

    
'''

# ------------ Q3 Write a program to find the square root of a number

"""

from math import *

number = int(input("Enter the number: "))
print(sqrt(number))


M2 without using sqrt fn.

num_sqrt = num ** 0.5

(num)^1/2

"""


# 21-oct-24 12:11 PM 
# ------------ Q4 Write a program to find the area of a triangle.

'''

base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))

area = 0.5 * base * height

print(area)

'''

# ------------ Q5 Write a program to check if a number is a palindrome.

'''

number = input("Enter the number to be checked: ")

ran = len(number)

i = 0
j = ran-1

pali = True

while i < j:
    if number[i] == number[j]:
        i += 1
        j -= 1
    else:
        pali = False
        break

if pali:
    print("Palindrome num")

else:
    print("not a Palindrome num")

'''



# ------------ Q6 Write a program to convert temperatures from Celsius to Fahrenheit.

'''

temp_c = float(input("Enter the temperature in Celsius: "))

temp_f = (temp_c * (9/5)) + 32

print("The temperature in Fahrenheit is: ", temp_f)

'''

# ------------ Q7 Write a program to calculate the factorial of a number.

'''

number = int(input("Enter the number: "))

i, fact = 1, 1

while i != number:

    fact *= i
    i += 1

print("Factorial of", number, "is: ", fact)

'''

# ------------ Q8 Write a program to find the greatest of three numbers.

'''
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
largest = 0


# M1

if (number1 >= number2) and (number1 >= number3):
    largest = number1

elif (number2 >= number1) and (number2 >= number3):
    largest = number2

else:
    largest = number3

print(largest)


# M2
# print(max(number1, number2, number3))

'''

# ------------ Q9 Write a program to print all prime numbers between 1 and 100.


'''

for i in range(2, 101):

    flag = True
    
    for j in range(2, i):
        if (i % j) == 0:
            flag = False
            break

    if (flag == True):
        print(i)

'''

# ------------ Q10 Write a program to generate a Fibonacci sequence up to n terms.

'''

n = int(input("enter the value of n: "))

second_last, last = 0, 1
ans = [0, 1]

for i in range(1, n+1): 

    curr = second_last + last
    ans.append(curr)
    second_last = last
    last = curr

print(ans)

'''