# 23-oct-24 10 PM 
# Strings

# ------------ Q1 Write a program to find the length of a string without using len().

'''

str = input("Enter the string: ")
count = 0

for i in str:
    count += 1

print("Length of string is:", count)

'''

# ------------ Q2 Write a program to check if two strings are anagrams.

'''

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

lst1 = list(str1)
lst1.sort()

lst2 = list(str2)
lst2.sort()

if lst1 == lst2:
    print("Anagram")
else:
    print("Not an Anagram")

'''

# ------------ Q3 Write a program to remove vowels from a string.

'''

str = input("Enter the string: ")
ans = ""

for i in range(0, len(str)):
    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
        continue
    else:
        ans += str[i]

print(ans)

'''

# ------------ Q4 Write a program to count the number of words in a string.

'''

str = input("Enter the string: ")
count = 0

for i in range(0, len(str)):
    if str[i] == " ":
        count += 1

print("number of words in a string is:", count+1)


'''


# ------------ Q5 Write a program to replace all spaces with underscores in a string.

'''

str = input("Enter the string: ")
ans = ""

for i in range(0, len(str)):
    if str[i] == " ":
        ans += "_"
    else:
        ans += str[i]

print(ans)

'''

# ------------ Q6 Write a program to find the longest word in a sentence.

'''

str = input("Enter the string: ")
word_count, maxx_count, strss, lar_str = 0, 0, "", ""

for i in range(0, len(str)):

    if str[i] == " ":
        word_count = 0
        strss = ""
    else:
        word_count += 1
        strss += str[i]

    if word_count > maxx_count:
        lar_str = strss


print(lar_str)

'''


# ------------ Q7 Write a program to check if a string contains only digits.

'''

str = input("Enter the string: ")

print(str.isnumeric())

'''


# ------------ Q8 Write a program to remove the punctuation from a string.


'''

import string

str = input("Enter the string: ")
ans = ""

for i in str:
    if i not in string.punctuation:
        ans += i

print(ans)

'''

