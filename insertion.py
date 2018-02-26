from random import randint

MAX_INT = 99999
N = 10000

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

def main():
    lst = []
    for i in range(10000):
        lst.append(randint(0, MAX_INT))    

    expected = sorted(lst)
    insertion_sort(lst)
    print(expected == lst)
    
            
if __name__ == "__main__":
    main()
