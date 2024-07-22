"""Dummy challenge for Kitt Demo"""
from math import pi


def circle_area(radius):
    """Returns the area of the circle of given radius"""
    return pi * radius**2 if radius > 0 else 0 # shorter way
