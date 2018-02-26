from random import randint, shuffle

MAX_INT = 99999
N = 10

"""
Bogosort
O((n + 1)!)
This is one of the worst sorting algorithms *ever*
"""
def bogo_sort(lst):
    while not in_order(lst):
        shuffle(lst)    
    
def in_order(lst):
    n = len(lst)
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

    
def main():
    lst = []
    for i in range(N):
        lst.append(randint(0, MAX_INT))    

    expected = sorted(lst)
    bogo_sort(lst)
    print(expected == lst)
    
            
if __name__ == "__main__":
    main()
