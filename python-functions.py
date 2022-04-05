#1 Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  return int(n * (n+1)/2)

#print(sum_to(10))

#2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(array):
  return max(array)

# print(largest([10, 4, 2, 231, 91, 54]))

#3 Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(str1,str2):
  appears = str1.count(str2)
  return appears

# print(occurances('fleep floop', 'p') )
  

#4 Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*nums):
  import math
  return math.prod(nums)