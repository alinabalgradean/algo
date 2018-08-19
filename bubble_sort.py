def MyBubbleSort(lst):
  """Unoptimized version of the bubble sort algorithm.
  
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
  """Optimized version of the bubble sort algorithm.
  
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
