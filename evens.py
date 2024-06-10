def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message :"A list was not passed into the function"
    if numbers is empty return False
    if the number of even number is odd, return False
    if the number of numbers is 0, return False
    if the number of even numbers is even, return True
    """
    # Refactoring the code 
    # we can optimise the code again 
    if isinstance(numbers, list):
        # in fact, the following line is useless, because even the list is empty it will return false at the end
#        if numbers == []:
#           return False
#         else: 
        evens = sum([1 for n in numbers if n % 2==0])
        #using list comprehension to refactor the code
        

        #for n in numbers:
        #    if n % 2==0:
        #        evens+=1
        
        #if evens:
        #    return evens % 2 == 0
        #return False

        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")



"""
when python runs a file directly it considers it as main file which is not the case here. But we
want python to run only the things which we test, that is why we need to tell python
which file is our main file.
"""
if __name__ =='__main__':
    print(even_number_of_evens([2,1,4]))