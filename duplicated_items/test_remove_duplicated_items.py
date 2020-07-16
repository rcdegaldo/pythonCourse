import unittest
from remove_duplicated_items import remove_duplicated_items

#IMPORTANT:
#All test functions must start with test_
#unittest Assertion Methods: https://docs.python.org/3/library/unittest.html#assert-methods


class TestGuess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Use setUpClass to run code at the beginning of the test Suite
        pass
  
    @classmethod
    def tearDownClass(cls):
        #Use tearDownClass to run code at the end of the test Suite
        pass

    def setUp(self):
        #Use setUp function to run code before each test case
        pass
  
    def tearDown(self):
        #Use setUp function to run code after each test case
        pass

    def test_all_duplicated_items_are_removed(self):
        list1 = ['a','b','b','c','d','b','a','b','a','b','b','c','d','b','a','b','c','d','b','a']
        list1_without_duplicated_items = ['a','b','c','d']
        
        result = remove_duplicated_items(list1)

        list1_without_duplicated_items.sort()
        result.sort()

        self.assertEqual(list1_without_duplicated_items, result, 'Result should be the list without duplicated items')

#With the below function we can run the tests with 'python test_remove_duplicated_items.py'
#Without this function we would have to do 'python -m unittest test_remove_duplicated_items.py'
if __name__ == '__main__':
    unittest.main()