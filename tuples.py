# 25-oct-24 4 PM 
# Tuples

# ------------ Q1 Write a program to create a tuple and print its elements.

'''

tple = ("car", "bus", "bike")
print(tple)

'''

# ------------ Q2 Write a program to find the length of a tuple.

'''

tple = ("car", "bus", "bike")
print(len(tple))

'''

# ------------ Q3 Write a program to find the maximum and minimum elements in a tuple.

'''

tple = (1, 2, 3, 4, 5)
maxx, minn = 0, 99999999

for x in tple:
    maxx = max(maxx, x)
    minn = min(minn, x)
      
print(maxx, " ", minn)

'''

# ------------ Q4 Write a program to check if an element exists in a tuple.

'''

tple = (1, 2, 3, 4, 5)
key = 5

if key in tple:
    print(True)

'''

# ------------ Q5 Write a program to convert a list into a tuple.

'''

lst = [1, 9, 10, 12]
tuple = ()

for x in lst:
    tuple += (x,)

print(tuple)

'''

# ------------ Q6 Write a program to find the sum of elements in a tuple.

'''

tple = (1, 2, 3, 4, 5)
sum = 0

for x in tple:
    sum += x
      
print(sum)

'''

# ------------ Q7 Write a program to concatenate two tuples.

'''

tuple1, tuple2 = (1, 2, 3, 4, 5), (1, 2, 3)
tuple3 = ()

for x in tuple1:
    tuple3 += (x,)
for x in tuple2:
    tuple3 += (x,)

print(tuple3)

'''

# ------------ Q8 Write a program to convert a tuple to a string.

'''

tuple1, string = (1, 2, 3, 4, 5), ""

for x in tuple1:
    string += str(x)

print(string)

'''

# ------------ Q9 Write a program to slice a tuple.

'''

tuple1, new_tuple = (1, 2, 3, 4, 5), ()

new_tuple = tuple1[0:4]
print(new_tuple)

'''

# ------------ Q10 Write a program to find the index of an element in a tuple.

'''

tuple1 = (1, 2, 3, 4, 5)
x = 5

for i in range(0, len(tuple1)):
    if x == tuple1[i]:
        print(i)
        break

'''
