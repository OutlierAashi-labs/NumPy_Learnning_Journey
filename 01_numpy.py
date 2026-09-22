#1    ************-----------------------------------------***************

'''
Arrays and Types of Arrays

Types of Arrays [Matrix]
1) One_dimensional Array
2) Two_dimensional Array
3) Three_dimensional Array
4) Multi_dimensional Array


'''

import numpy as np

marks = [23,90,87,76,92]
print(marks)

# Types

# 1d
ar_1d = np.array([23,90,87,76,92])
print(ar_1d)

# 2d or Multi - dimensional Array

ar_2d = np.array([[23,89,67],[56,89,9],[87,63,21]])
print(ar_2d)


'''
Output 

[23, 90, 87, 76, 92]
[23 90 87 76 92]
[[23 89 67]
 [56 89  9]
 [87 63 21]]


'''

#2  ************-----------------------------------------***************

'''
**Create an Array**

 1 Creating arrays from python lists

  ar = np.array([])

2 with default value

a) Zeros
np.zeros(shape) ,
b) Ones
np.ones((shape)) ,
c) agar kisi specific number se fill  ho default value ( full(shape,value)
np.full((2,2),6)

'''

# 1 Array create by python list
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(arr)

# 2 Array Create by python list
# a) zeros
zeroes_array = np.zeros(3)
print(zeroes_array)

# b) ones
Ones_array = np.ones((2,3))
print(Ones_array)

# c) full
fill_arr = np.full((3,3),5)
print(fill_arr)


'''
Output

[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
[0. 0. 0.]
[[1. 1. 1.]
 [1. 1. 1.]]
[[5 5 5]
 [5 5 5]
 [5 5 5]]

'''

#3   ************-----------------------------------------***************

'''
**Creating sequences**

arange(start,stop,step)

'''

import numpy as np
arr = np.arange(1,10,3)
print(arr)

'''
Output
[1 4 7]

'''

#4   ************-----------------------------------------***************

'''
**Creating identity matrices**

eye(size)

'''

import numpy as np
identity_matrix = np.eye(2)
print(identity_matrix)


'''
Output

[[1. 0.]
 [0. 1.]]

'''

#5 ************-----------------------------------------***************

'''

**Attributes or Properties of Arrays**

1 Shape -- number of (rows,column)

2 size -- number of elements

3 ndim -- number of dimensions

4 .dtype -- datatype of elements

'''

import numpy as np

arr_2d = np.array([[1,2,7],[3,4,9]])
print(arr_2d.shape)

arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr.size)

arr_1d = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
arr_2d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[3,4],[6,7],[1,3],[2,4]]])
print(arr_1d)
print(arr_1d.ndim)
print(arr_2d)
print(arr_2d.ndim)
print(arr_3d)
print(arr_3d.ndim)

arr = np.array([1,2,3,4,5,6,7,8,9,0,11,14.9])
print(arr.dtype)

'''
Output

(2, 3)
9
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
1
[[1 2 3]
 [4 5 6]]
2
[[[3 4]
  [6 7]
  [1 3]
  [2 4]]]
3
float64

'''

#6  ************-----------------------------------------***************
'''
Change Data Type in Array
'''

import numpy as np

arr = np.array([1.2,2.5,3.8])
print(arr)
print(arr.dtype)
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)

arr1 = np.array([12,25,38])
print(arr1.dtype)
float_arr = arr.astype(float)
print(float_arr)
print(float_arr.dtype)

'''
Output
[1.2 2.5 3.8]
float64
[1 2 3]
int64
int64
[1.2 2.5 3.8]
float64
'''

#7   ************-----------------------------------------***************

'''
**OPERATOR** :

1 +

2 -

3 *

4 /

5 **

6 //

7 %

'''

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr + 5)
print(arr - 5)
print(arr * 5)
print(arr / 5)
print(arr ** 5)
print(arr // 5)
print(arr % 5)

'''
Output
[ 6  7  8  9 10]
[-4 -3 -2 -1  0]
[ 5 10 15 20 25]
[0.2 0.4 0.6 0.8 1. ]
[   1   32  243 1024 3125]
[0 0 0 0 1]
[1 2 3 4 0]

'''

#8    ************-----------------------------------------***************

'''
**Aggregation Function (Summarise)**

FUNCTIONS

1 sum -- add all

2 mean -- calculate average

3 min --  calculate min

4 max -- calculate max

5 std -- calculate standard deviation

6 var -- calculate variance

'''

import numpy as np
arr = np.array([1,2,3,4,5])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))

'''
Output

15
3.0
1
5
1.4142135623730951
2.0
'''

#9 

'''

INDEXING

array[index] -- 1d array

array[row,column] -- 2d array

SLICING

Fancy Indexing

Boolean Masking

RESHAPING

'''

import numpy as np

# Indexing
arr = np.array([1,2,3,4,5])
print(arr[1])
print(arr[2])
print(arr[-1])

# Slicing
# array[start:stop:step]

arr = np.array([10,20,30,40,50,60])
print(arr[1:5])
print(arr[:4])
print(arr[2:])
print(arr[::2])
print(arr[::-1])
print(arr)

# Fancy Indexing
# Selecting multiple elements at once

print(arr[[0,2,4]])

# Boolean masking
# condition -- True , False

print(arr[arr>55])

# Reshaping -- change 1d in multidimensional arrays
# Reshaping  means change dimension or shape of array without modifying the data or without changing the number of element .
# We can reshape (rows,columns) only if dimension match
# Reshaping does not create copy , its create view

reshaped_Arr = arr.reshape(3,2)
print(reshaped_Arr)
print(arr)

# flatten()
# change multidimensional in 1d
# .ravel() -> view            modification in original array
# .flatten() -> copy          no modification

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d.ravel())
print(arr_2d.flatten())


'''
Output

2
3
5
[20 30 40 50]
[10 20 30 40]
[30 40 50 60]
[10 30 50]
[60 50 40 30 20 10]
[10 20 30 40 50 60]
[10 30 50]
[60]
[[10 20]
 [30 40]
 [50 60]]
[10 20 30 40 50 60]
[1 2 3 4 5 6 7 8 9]
[1 2 3 4 5 6 7 8 9]

'''
