from random import randint

MAX_INT = 99999

# destructive
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

    
lst = []
for i in range(10000):
    lst.append(randint(0, MAX_INT))    

expected = sorted(lst)
insertion_sort(lst)
print(expected == lst)
