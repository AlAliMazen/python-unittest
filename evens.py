def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message :"A list was not passed into the function"
    if numbers is empty return False
    if the number of even number is odd, return False
    if the number of numbers is 0, return False
    if the number of even numbers is even, return True
    """
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else: 
            evens = 0
        
        for n in numbers:
            if n % 2==0:
                evens+=1
        
        if evens:
            return evens % 2 == 0
        return False
    else:
        raise TypeError("A list was not passed into the function")



"""
when python runs a file directly it considers it as main file which is not the case here. But we
want python to run only the things which we test, that is why we need to tell python
which file is our main file.
"""
if __name__ =='__main__':
    print(even_number_of_evens(5))