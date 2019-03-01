# MathFunctions.py

import math

def areaCircle(radius):
	area = math.pi * radius * radius
	return area

def areaSquare(side):
	area = side * side
	return area

def areaRectangle(length, width):
	area = length * width
	return area

def x_numbers(number1, number2, number3):
	x = (number1, number2, number3)
	return x

def y_numbers(number1, number2, number3):
	y = (number1, number2, number3)
	return y

	from pylab import plot, show
	plot(x_numbers, y_numbers)

