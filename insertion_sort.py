def InsertionSort(lst):
  """Basic Insertion sort.
  
  Args:
    lst [list]: The list to be sorted.
    
  Returns:
    lst [list]: Sorted list.
  """
  for index in range(1, len(lst)):
  
    position = index
    temp_value = array[lst]
  
    while position > 0 and lst[position - 1] > temp_value:
      lst[position] = lst[position - 1]
      position -= 1
  
    lst[position] = temp_value
    
  return lst
