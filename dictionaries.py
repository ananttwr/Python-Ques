# 24-oct-24 4 PM 
# Dictionaries

# ------------ Q1 Write a program to create a dictionary from two lists.

'''

lst1, lst2 = [2, 4, 5, 5, 6, 7, 7, 8], [2, 3, 5, 7]
dict = {}

for i in range(0, len(lst1)):
    if lst1[i] in dict:
        dict[lst1[i]] += 1
    else:
        dict[lst1[i]] = 1

for i in range(0, len(lst2)):
    if lst2[i] in dict:
        dict[lst2[i]] += 1
    else:
        dict[lst2[i]] = 1

print(dict)

'''

# ------------ Q2 Write a program to merge two dictionaries.

'''

dict1, dict2 = {'a': 2, 'b': 1}, {'c': 3, 'd': 5}

dict2.update(dict1)

print(dict2)

'''

# ------------ Q3 Write a program to check if a key exists in a dictionary.

'''

dict1 = {'a': 2, 'b': 1}
key, ans = 'a', False

if key in dict1:
    ans = True


print(ans)

'''

# ------------ Q4 Write a program to sort a dictionary by its values.

'''

dict1 = {'a': 2, 'c': 2, 'b': 1}

Keys = list(dict1.keys())
Keys.sort()

new_dict = {i: dict1[i] for i in Keys}

print(new_dict)

'''


# ------------ Q5 Write a program to add a new key-value pair to a dictionary.

'''

dict1 = {'a': 2, 'c': 2, 'b': 1}

dict1['d'] = 1

print(dict1)

'''

# ------------ Q6 Write a program to delete a key from a dictionary.

'''

dict1 = {'a': 2, 'c': 2, 'b': 1}

del dict1['b']

print(dict1)

'''

# ------------ Q7 Write a program to find the maximum and minimum value in a dictionary.

'''

dict1 = {'a': 2, 'c': 2, 'b': 1}

minn = min(dict1.values())
maxx = max(dict1.values())

print(minn, maxx)

'''

# ------------ Q8 Write a program to invert a dictionary (swap keys and values).

'''

dict1 = {'a': 2, 'c': 2, 'b': 1}
inv_dict = {}

for key, value in dict1.items():

    inv_dict[value] = key

print(inv_dict)

'''

# ------------ Q9 Write a program to count the frequency of characters in a string using a dictionary.

'''

str = input("Enter the string: ")
freq = {}

for i in range(0, len(str)):
    if str[i] in freq:
        freq[str[i]] += 1
    else:
        freq[str[i]] = 1

print(freq)

'''

# ------------ Q10 Write a program to find the common keys in two dictionaries.

'''

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'c': 2}
ans = []

for key in dict1.items():
    if key in dict2.items():
        ans.append(key)

print(ans)

'''