from random import randint

MAX_INT = 99999
N = randint(8000, 12000)

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

"""
Iterative Merge Sort
"""
def iter_merge_sort(lst):
    print("TODO: Implement")
    
def main():
    lst = []
    for i in range(N):
        lst.append(randint(0, MAX_INT))    

    expected = sorted(lst)
    lst = merge_sort(lst)
    print(expected == lst)
    
            
if __name__ == "__main__":
    main()
