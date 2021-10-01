# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Successive Approximation
#
#
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print(evaluate_poly(poly, x))  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO ...
    def evaluate_poly(poly, x):
    
    val = 0
    for a in range(0,len(poly)):
        val = val + (poly[a] * pow(x,a))
    return val
x=-13
poly=(0.0,0.0,5.0,9.3,7.0)
print(evaluate_poly(poly,x))



def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print(compute_deriv(poly))        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ...
    def compute_deriv(poly):
        derivative_tuple=()
    for a in range(1,len(poly)):
        val=(a*poly[a])
        derivative_tuple=derivative_tuple+(val,)
    return derivative_tuple
poly=(-13.39,0.0,17.5,3.0,1.0)
print(compute_deriv(poly))


def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print(compute_root(poly, x_0, epsilon))
    (0.806790753796352, 8)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ...
    def compute_root(poly, x_0, epsilon):
        iteration_counter=1
    while(abs(evaluate_poly(poly,x_0))>epsilon):
        iteration_counter+=1
        x_0=x_0-(evaluate_poly(poly,x_0)/(evaluate_poly(compute_deriv(poly),x_0)))
    return(x_0,iteration_counter)

poly=(0.0,0.0,5.0,9.3,7.0)
x=-13
print(evaluate_poly(poly,x))
poly=(-13.3,0.0,17.5,3.0,1.0)
print(compute_deriv(poly))
x_0=0.1
epsilon=0.0001
print(compute_root(poly,x_0,epsilon))
        

