# Enter you module contents here
'''
Create your own module as file triangle.py in the src folder. The module should contain two functions:

hypothenuse which returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle
area which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
Make sure both the functions and the module have descriptive docstrings. Add also the __version__ and __author__ attributes to the module. Call both your functions from the main function (which is in file usemodule.py).


'''
import math

__version__ = "1.0"
__author__ = "Hiroshi Doyu"

# hypothenuse which returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle
def hypothenuse(w, h):
    '''
    hypothenuse() function
    '''
    return math.sqrt(w**2 + h**2)

# area which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
def area(w, h):
    '''
    area() function
    '''
    return w * h / 2
