"""This problem was asked by Google.

The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x² + y² = r²."""

from random import uniform

def circle(x, y, r=1):
    """(Int,Int) => Boolean
    given an x and y returns:
    - True if coordinates are inside circle of radius r centered on (0,0)
    - False otherwise"""
    return x**2 + y**2 <= r**2

def random_point(low=-1, high=1):
    return (uniform(low, high), uniform(low, high))

def pi_estimate(nb_points=2**25):
    """estimates area of circle of radius 1 inscribed in square of len 2 with
    Monte Carlo method, estimates pi from circle area"""
    res = 4 * sum((circle(*random_point()) for i in range(nb_points)))/nb_points
    return res

def test_circle():
    assert circle(0, 0)
    assert circle(1, 0)
    assert not circle(1, 1)

def test_pi_estimate():
    for i in range(5):
        assert round(pi_estimate(),3) == 3.142
