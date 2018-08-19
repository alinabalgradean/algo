import timeit
import random

def MyBubbleSort(lst):
  """Simple un-optimized version of the bubble sort algorithm.
  
  The elements of the list are sorted in-place. Highly 
  inefficient, with O(n^2).
  
  Args:
    lst [list]: The list to be sorted.
    
  Returns:
    lst [list]: Sorted list.
  """
  n = len(lst)
  
  for i in range(n):
    for j in range(n-1):
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        
  return lst
  
def MyBubbleSortSlighlyOptimized(lst):
  """Simple slightly optimized version of the bubble sort algorithm.
  
  The elements of the list are sorted in-place. Highly 
  inefficient, with O(n^2).
  
  Args:
    lst [list]: The list to be sorted.
    
  Returns:
    lst [list]: Sorted list.
  """
  n = len(lst)
  
  for i in range(n):
    for j in range(n-i-1):
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        
  return lst

# 10,000 elements unsorted list - Result below

# Around ~ 113 sec for the best running time
print min(timeit.Timer(stmt='sorted_lst=MyBubbleSort(simple_lst)',
                       setup=setup).repeat(3, 10))
# Around ~ 60 sec for the best running time
print min(timeit.Timer(stmt='sorted_lst=MyBubbleSortSlighlyOptimized(simple_lst)',
                       setup=setup).repeat(3, 10))
# < 0.03 sec for the best running time
print min(timeit.Timer(stmt='sorted_lst=sorted(simple_lst)',
                       setup=setup).repeat(3, 10))
