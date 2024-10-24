# 24-oct-24 7:20 PM 
# Sets

# ------------ Q1 Write a program to find the union of two sets.

'''

set1, set2 = {1, 2, 3}, {14, 5, 6}
set1.update(set2)

print(set1)

'''

# ------------ Q2 Write a program to find the intersection of two sets.

'''

set1, set2 = {1, 2, 3}, {14, 3, 6}
ans = []

for x in set1:
    if x in set2:
        ans.append(x)

print(ans)

'''


# ------------ Q3 Write a program to find the difference between two sets.

'''

set1, set2 = {1, 2, 3}, {14, 3, 6}
ans = []

for (x, y) in zip(set1, set2):
    ans.append(x-y)

print(ans)

'''

# ------------ Q4 Write a program to check if one set is a subset of another.

'''

set1, set2 = {1, 2, 3}, {4, 3}

print(set2.issubset(set1))

'''


# ------------ Q5 Write a program to remove duplicates from a list using a set.

'''

lst = [1, 2, 2, 3, 4, 4]
st = set()

for i in lst:
    st.add(i)

print(st)

'''

# ------------ Q6 Write a program to check if two sets are disjoint.

'''

set1, set2 = {1, 2, 3}, {4, 6}
ans = True

for x in set1:
    if x in set2:
        print("Not Disjoint")
        ans = False
        break


if ans == True:
    print("Disjoint")

'''


# ------------ Q7 Write a program to create a set of squares of numbers from 1 to 10.

'''

sq_set = set()

for i in range(1, 11):
    sq_set.add(i*i)

print(sq_set)

'''

# ------------ Q8 Write a program to find the symmetric difference between two sets.

'''

set1, set2 = {1, 2, 3}, {3, 6}
ans = []

for x in set1:
    if x not in set2:
        ans.append(x)

print(ans)

'''

# ------------ Q9 Write a program to check if a set is empty.

'''

st = set()
st = {}
count = 0

for x in st:
    count += 1

if count > 0:
    print("Set is not empty")

else:
    print("Set is empty")

'''


# ------------ Q10 Write a program to convert a set to a list.

'''

set = {1, 2, 4}
lst = []

for i in set:
    lst.append(i)

print(lst)

'''
