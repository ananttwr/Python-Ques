# 22-oct-24 12:42 PM 
# Functions


# ------------ Q1 Write a function to find the maximum of two numbers.

'''

def sum(a, b):
    print("Sum of a and b is:", a+b) 

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

sum(n1, n2)


'''

# ------------ Q2 Write a function to find the greatest common divisor (GCD) of two numbers.

'''

def gcd(a, b):

    gcd_curr = 1

    for i in range(1, min(a, b)+1):
        if ((a%i) == 0) and ((b%i) == 0):
            gcd_curr = max(gcd_curr, i)
    

    print("GCD of a and b is", gcd_curr)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

gcd(n1, n2)

'''

# ------------ Q3 Write a function to convert decimal numbers to binary.

'''

def dec_bin(n):
    ans = ""
    while n > 0:
        rem = n % 2
        ans += str(rem)
        n //= 2

    rev = ans[::-1]       # for reversing string, [start:end:step], start and end empty means whole string, -1 means 1 step back

    print(rev) 

n = int(input("Enter the number in decimal form: "))

dec_bin(n)

'''

# ------------ Q4 Write a function to calculate the power of a number.

'''

def power(a, b):
    ans = 1
    for i in range(1, b+1):
        ans *= a

    print(ans)

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the power: "))

power(n1, n2)


'''

# ------------ Q5 Write a function to calculate the sum of all elements in a list.

'''

def sum(n):
    lst = []
    sum = 0

    for i in range(0, n):
        ele = int(input("Enter the list items: "))
        lst.append(ele)
        sum += i
    
    print("The list is:", lst)
    print("The sum of list element is:", sum)


n = int(input("Enter the number of items in list: "))
sum(n)
    
'''

# ------------ Q6 Write a function to check if a string is a palindrome.

'''

def palidrome_check(string):

    n = len(string)
    i, j = 0, n-1
    flag = True

    while i < j:
        if string[i] != string[j]:
            flag = False
            print("Not a palindrome.")
            break
        else:
            i += 1
            j -= 1

    if flag == True:
        print("Palindrome.")


string = input("Enter the string to be checked: ")
palidrome_check(string)

'''

# ------------ Q7 Write a function to calculate the average of numbers in a list.


'''

def avg(n):
    lst = []
    sum = 0

    for i in range(0, n):
        ele = int(input("Enter the list items: "))
        lst.append(ele)
        sum += i
    
    avg = sum / n

    print("The list is:", lst)
    print("The average of list elements is:", avg)


n = int(input("Enter the number of items in list: "))
avg(n)

'''

# ------------ Q8 Write a function to find the largest element in a list.

'''

def largest_ele(n):
    lst = []
    maxx = 0

    for i in range(0, n):
        ele = int(input("Enter the list items: "))
        lst.append(ele)
        maxx = max(ele, maxx)

    print("The list is:", lst)
    print("The largest element in the list is: ", maxx)


n = int(input("Enter the number of items in list: "))
largest_ele(n)

'''

# ------------ Q9 Write a function to return the reverse of a string.

'''

def reverse_str(str):

    n = len(str)
    ans = ""
    for i in range(n-1, 0-1, -1):
        ans += str[i]

    print("Reverse of string is:", ans)


str = input("Enter the string: ")
reverse_str(str)

'''

# ------------ Q10 Write a function to count the number of vowels in a string.

'''

def vowel_count(str):

    n = len(str)
    count = 0

    for i in range(0, n):
        if (str[i] == 'a') or (str[i] == 'e') or (str[i] == 'i') or (str[i] == 'o') or (str[i] == 'u'): 
            count += 1

    print("Number of vowel in the string is:", count)


str = input("Enter the string: ")
vowel_count(str)

'''