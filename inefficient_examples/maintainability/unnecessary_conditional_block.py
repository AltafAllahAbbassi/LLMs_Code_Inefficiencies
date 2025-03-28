# HumanEval/92 by DeepSeek-Coder-6.7B
# the conditional block can be removed and replaced by can be removed and replaced with a single return statement that directly evaluates and returns the result of the given condition 

def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    if x == y + z and type(x) == int and type(y) == int and type(z) == int:
        return True
    else:
        return False