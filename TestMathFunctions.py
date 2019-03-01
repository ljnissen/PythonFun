# TestMathFunctions.py

# Import statements

import unittest
import MathFunctions

class KnownValues(unittest.TestCase):
	# Test areaCircle() pi r*r

	def test_areaCircle_for_10radius(self):
		# Capture the results of the function
		result = MathFunctions.areaCircle(10)
		# Check for expected output
		expected = 314.1592653589793
		self.assertEqual(expected, result)

	def test_areaCircle_for_2radius(self):
		# Capture the results of the function
		result = MathFunctions.areaCircle(2)
		# Check for expected output
		expected = 12.566370614359172
		self.assertEqual(expected, result)

	def test_areaCircle_for_500radius(self):
		# Capture the results of the function
		result = MathFunctions.areaCircle(500)
		# Check for expected output
		expected = 785398.1633974483
		self.assertEqual(expected, result)

	def test_areaSquare_for_10side(self):
		# Capture the results of the function
		result = MathFunctions.areaSquare(10)
		# Check for expected output
		expected = 100
		self.assertEqual(expected, result)

	def test_areaSquare_for_50side(self):
		# Capture the results of the function
		result = MathFunctions.areaSquare(50)
		# Check for expected output
		expected = 2500
		self.assertEqual(expected, result)

	def test_areaRectangle_for_10_50_sides(self):
		# Capture the results of the function
		result = MathFunctions.areaRectangle(10, 50)
		# Check for expected output
		expected = 500
		self.assertEqual(expected, result)

	def test_x_numbers_for_1_2_3(self):
		# Capture the results of the function
		result = MathFunctions.x_numbers(1, 2, 3)
		# Check for expected output
		expected = (1, 2, 3)
		self.assertEqual(expected, result)

	def test_y_numbers_for_2_4_6(self):
		# Capture the results of the function
		result = MathFunctions.y_numbers(2, 4, 6)
		# Check for expected output
		expected = (2, 4, 6)
		self.assertEqual(expected, result)

# Run the Tests

if __name__ == '__main__':
	unittest.main()
