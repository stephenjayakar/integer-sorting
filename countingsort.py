from random import randint

MAX_INT = 99999
N = randint(8000, 12000)

"""
Non-destructive Counting Sort
O(n + k) time, k is the range of values
Pretty great if the range is small, though
 often the range can be massive (like 2^32)
"""
def counting_sort(lst):
    # also, make this in the range from min -> max instead of 0 -> max
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
    
def main():
    lst = []
    for i in range(N):
        lst.append(randint(0, MAX_INT))    

    expected = sorted(lst)
    lst = counting_sort(lst)
    print(expected == lst)
    
            
if __name__ == "__main__":
    main()
