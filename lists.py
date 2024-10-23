# 23-oct-24 2:19 PM 
# Lists

# ------------ Q1 Write a program to create a list of the first 10 even numbers.

'''

lst_even = []
count = 0
i = 1

while count < 10:
    if i % 2 == 0:
        lst_even.append(i)
        count+=1

    i += 1 
    
print("even numbers are: ", lst_even)

'''

# ------------ Q2 Write a program to remove duplicates from a list.

'''

lst = [2, 4, 5, 5, 6, 7, 7]

n = len(lst)
st = set()

for i in range(0, n):
    st.add(lst[i])

print(st)

'''

# ------------ Q3 Write a program to find the second-largest number in a list.

'''

lst = [2, 4, 5, 5, 6, 7, 7, 8]

n, max1, max2 = len(lst), 0, 0

for i in range(0, n):
    max1 = max(max1, lst[i])

for i in range(0, n):
    if (lst[i] != max1):
        max2 = max(max2, lst[i])

print(max2)

'''

# ------------ Q4 Write a program to merge two sorted lists into one sorted list.

'''

lst1, lst2, ans = [2, 4, 5, 5, 6, 7, 7, 8], [2, 3, 5, 7], []

ans = lst1 + lst2
ans.sort()

print(ans)

'''

# ------------ Q5 Write a program to find the frequency of each element in a list.

'''

lst1 = [2, 4, 5, 5, 6, 7, 7, 8]
freq = {}

for item in lst1:
    if(item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)

'''

# ------------ Q6 Write a program to check if two lists are equal.

'''

lst1, lst2 = [2, 4, 5, 5, 6, 7, 7, 8], [2, 4, 5, 5, 6, 7, 7, 8]

if lst1 == lst2:
    print("equal")
else:
    print("not equal")

'''

# ------------ Q7 Write a program to flatten a nested list.

'''

lst1, ans = [[2, 4, 5], [5, 6, 7], [7, 8]], []

for i in range(0, len(lst1)):
    for j in range(0, len(lst1[i])):
        ans.append(lst1[i][j])

print(ans)

'''

# ------------ Q8 Write a program to rotate a list by n positions.

'''

n = int(input("Enter the number of positions by which the list is to be rotated: "))

lst1, ans = [2, 4, 5, 5, 6, 7, 7, 8], []

for i in range(0+n, len(lst1)):
    ans.append(lst1[i])

for i in range(0, 0+n):
    ans.append(lst1[i])

print(ans)

'''

# ------------ Q9 Write a program to find the cumulative sum of elements in a list.





# ------------ Q10 Write a program to find the intersection of two lists.

'''

lst1, lst2, ans = [2, 4, 5, 5, 6, 7, 7, 8], [2, 4, 7, 7, 8], []
i, j = 0, 0

for i in range(0, len(lst2)):
    if lst2[i] in lst1:
        ans.append(lst2[i])

print(ans)

'''