import unittest
# to test the function in the other file we have first to import it

from evens import even_number_of_evens



# we have to import unittest header and inherit from it as well
# inherit from unittest.TestCase
class TestEvens(unittest.TestCase):
    # pass tells the interpreter to pass the obligation of having code after the colon
    pass
    # if we comment out pass python expects a code after the colon and will throw an error

    # any test must start with the word test_
    def test_function_return_true(self):
        # the self parameter gives access to the function and 
        # her we use assertTrue to see if function returns true-> just simple test
        self.assertTrue(even_number_of_evens([])) # it will fail because function returns None instead

unittest.main()


