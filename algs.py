from random import shuffle
"""
Bogosort
O((n + 1)!)
This is one of the worst sorting algorithms *ever*
"""
def bogo_sort(lst):
    while not _in_order(lst):
        shuffle(lst)
    
def _in_order(lst):
    n = len(lst)
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

"""
Destructive Insertion Sort
O(n^2) time 
This one kind of sucks :( 
"""
def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        val = lst[i]
        index = i - 1
        while index >= 0 and lst[index] > val:
            temp = lst[index]
            lst[index] = val
            lst[index + 1] = temp
            index -= 1            

"""
Non-destructive Counting Sort
O(n + k) time, k is the range of values
Pretty great if the range is small, though
 often the range can be massive (like 2^32)
"""
def counting_sort(lst):
    n = len(lst)
    # it would be faster to get the min and max at once
    max_val = max(lst)
    min_val = min(lst)
    count_buffer = [0] * (max_val - min_val + 1)
    for num in lst:
        count_buffer[num - min_val] += 1
    ret_lst = []
    for i in range(len(count_buffer)):
        v = count_buffer[i]
        if v != 0:
            ret_lst.extend([i + min_val] * v)
    return ret_lst        

"""
Non-destructive Merge Sort
O(n lg n) time 
The classic comparison-based sort!
"""
def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst    
    lst1 = merge_sort(lst[:n//2])
    lst2 = merge_sort(lst[n//2:])
    merged_list = []
    i1 = 0
    i2 = 0
    while i1 < len(lst1) and i2 < len(lst2):
        v1 = lst1[i1]
        v2 = lst2[i2]
        if v1 <= v2:
            merged_list.append(v1)
            i1 += 1
        else:
            merged_list.append(v2)
            i2 += 1
    # tailcase
    while i1 < len(lst1):
        v = lst1[i1]
        merged_list.append(v)
        i1 += 1
    while i2 < len(lst2):
        v = lst2[i2]
        merged_list.append(v)
        i2 += 1
    return merged_list

# implement timsort

# implement bubblesort
