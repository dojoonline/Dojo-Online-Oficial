import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
	
	def test_divisor_por_3(self):
		r = fizzbuzz(3)
		self.assertEqual(r.fizzbuzz(), "fizz")
	def test_divisor_por_5(self):
		d = fizzbuzz(5)	
		self.assertEqual(d.fizzbuzz(), "buzz")
	def test_divisor_por_15(self):
		parabens = fizzbuzz(15)
		self.assertEqual(parabens.fizzbuzz(),"fizzbuzz")
if __name__ == '__main__':
	unittest.main()
