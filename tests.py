from algs import bogo_sort, insertion_sort, counting_sort, merge_sort
from random import randint
import unittest

class TestSorts(unittest.TestCase):
    def test_bogo(self):
        MAX_INT = 99999
        N = 5
        lst = []
        for i in range(N):
            lst.append(randint(0, MAX_INT))    

        expected = sorted(lst)
        bogo_sort(lst)
        self.assertEqual(expected, lst)

    def test_insertion(self):
        MAX_INT = 99999
        N = 1000
        lst = []
        for i in range(N):
            lst.append(randint(0, MAX_INT))    

        expected = sorted(lst)
        insertion_sort(lst)
        self.assertEqual(expected, lst)

    def test_counting(self):
        MAX_INT = 99999
        N = randint(8000, 12000)
        lst = []
        for i in range(N):
            lst.append(randint(0, MAX_INT))    

        expected = sorted(lst)
        lst = counting_sort(lst)
        self.assertEqual(expected, lst)

    def test_merge(self):
        MAX_INT = 99999
        N = randint(8000, 12000)
        lst = []
        for i in range(N):
            lst.append(randint(0, MAX_INT))    

        expected = sorted(lst)
        lst = merge_sort(lst)
        self.assertEqual(expected, lst)

        
if __name__ == "__main__":
    unittest.main()
