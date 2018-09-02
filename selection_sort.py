def MySelectionSort(lst):
  """Unoptimized version of the selection sort algorithm.
  
  Args:
    lst [list]: The list to be sorted.
    
  Returns:
    lst [list]: Sorted list.
  """
  n = len(lst)
  
  for i in range(n):
    
    wall = i
    for j in range(i+1, n):
      if lst[wall] > lst[j]:
        wall = j
        
  lst[wall], lst[i] = lst[i], lst[wall]
        
  return lst
