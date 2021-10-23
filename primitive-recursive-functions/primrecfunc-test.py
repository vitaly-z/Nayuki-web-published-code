# 
# Test suite for primrecfunc (Python).
# Runnable as a main program, which should print "All N tests passed".
# 
# Copyright (c) 2021 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/primitive-recursive-functions
# 

from typing import List, Tuple
from primrecfunc import *


TestCase = Tuple[List[int],int]  # (arguments, answer)
TestSuite = Tuple[PrimRecFunc,List[TestCase]]
testsuites: List[TestSuite] = [
	# Primitive functions
	(Z, [
		([0], 0),
		([1], 0),
		([2], 0),
		([5], 0),
	]),
	
	(S, [
		([0], 1),
		([1], 2),
		([2], 3),
		([5], 6),
	]),
	
	(I(1,0), [([0], 0), ([3], 3)]),
	(I(2,0), [([4, 5], 4)]),
	(I(2,1), [([4, 5], 5)]),
	(I(3,0), [([7, 8, 9], 7)]),
	(I(3,1), [([7, 8, 9], 8)]),
	(I(3,2), [([7, 8, 9], 9)]),
	
	# Boolean functions
	(prnot, [
		([0], 1),
		([1], 0),
	]),
	
	(prand, [
		([0, 0], 0),
		([0, 1], 0),
		([1, 0], 0),
		([1, 1], 1),
	]),
	
	(pror, [
		([0, 0], 0),
		([0, 1], 1),
		([1, 0], 1),
		([1, 1], 1),
	]),
	
	(prxor, [
		([0, 0], 0),
		([0, 1], 1),
		([1, 0], 1),
		([1, 1], 0),
	]),
	
	(mux, [
		([0, 0, 0], 0),
		([0, 0, 1], 1),
		([0, 1, 0], 0),
		([0, 1, 1], 1),
		([1, 0, 0], 0),
		([1, 0, 1], 0),
		([1, 1, 0], 1),
		([1, 1, 1], 1),
		([0, 3, 7], 7),
		([1, 3, 7], 3),
		([0, 5, 2], 2),
		([1, 5, 2], 5),
	]),
	
	# Comparison functions
	(z, [
		([0], 1),
		([1], 0),
		([2], 0),
		([5], 0),
	]),
	
	(nz, [
		([0], 0),
		([1], 1),
		([2], 1),
		([5], 1),
	]),
	
	(eq, [
		([0, 0], 1),
		([0, 1], 0),
		([0, 2], 0),
		([1, 0], 0),
		([1, 1], 1),
		([1, 2], 0),
		([2, 0], 0),
		([2, 1], 0),
		([2, 2], 1),
		([5, 0], 0),
		([6, 6], 1),
		([3, 7], 0),
	]),
	
	(neq, [
		([0, 0], 0),
		([0, 1], 1),
		([0, 2], 1),
		([1, 0], 1),
		([1, 1], 0),
		([1, 2], 1),
		([2, 0], 1),
		([2, 1], 1),
		([2, 2], 0),
		([5, 0], 1),
		([6, 6], 0),
		([3, 7], 1),
	]),
	
	(lt, [
		([0, 0], 0),
		([0, 1], 1),
		([0, 2], 1),
		([1, 0], 0),
		([1, 1], 0),
		([1, 2], 1),
		([2, 0], 0),
		([2, 1], 0),
		([2, 2], 0),
		([5, 0], 0),
		([6, 6], 0),
		([3, 7], 1),
	]),
	
	(le, [
		([0, 0], 1),
		([0, 1], 1),
		([0, 2], 1),
		([1, 0], 0),
		([1, 1], 1),
		([1, 2], 1),
		([2, 0], 0),
		([2, 1], 0),
		([2, 2], 1),
		([5, 0], 0),
		([6, 6], 1),
		([3, 7], 1),
	]),
	
	(gt, [
		([0, 0], 0),
		([0, 1], 0),
		([0, 2], 0),
		([1, 0], 1),
		([1, 1], 0),
		([1, 2], 0),
		([2, 0], 1),
		([2, 1], 1),
		([2, 2], 0),
		([5, 0], 1),
		([6, 6], 0),
		([3, 7], 0),
	]),
	
	(ge, [
		([0, 0], 1),
		([0, 1], 0),
		([0, 2], 0),
		([1, 0], 1),
		([1, 1], 1),
		([1, 2], 0),
		([2, 0], 1),
		([2, 1], 1),
		([2, 2], 1),
		([5, 0], 1),
		([6, 6], 1),
		([3, 7], 0),
	]),
	
	(even, [
		([0], 1),
		([1], 0),
		([2], 1),
		([3], 0),
		([4], 1),
		([5], 0),
	]),
	
	(odd, [
		([0], 0),
		([1], 1),
		([2], 0),
		([3], 1),
		([4], 0),
		([5], 1),
	]),
	
	(divisible, [
		([ 0, 0], 1),
		([ 1, 0], 0),
		([ 2, 0], 0),
		([ 0, 1], 1),
		([ 1, 1], 1),
		([ 2, 1], 1),
		([ 0, 2], 1),
		([ 1, 2], 0),
		([ 2, 2], 1),
		([ 3, 2], 0),
		([ 0, 3], 1),
		([ 1, 3], 0),
		([ 2, 3], 0),
		([ 3, 3], 1),
		([ 4, 3], 0),
		([ 5, 3], 0),
		([ 6, 3], 1),
		([ 7, 5], 0),
		([25, 5], 1),
	]),
	
	(prime, [
		([ 0], 0),
		([ 1], 0),
		([ 2], 1),
		([ 3], 1),
		([ 4], 0),
		([ 5], 1),
		([ 6], 0),
		([ 7], 1),
		([ 8], 0),
		([ 9], 0),
		([10], 0),
		([11], 1),
		([12], 0),
		([13], 1),
		([14], 0),
		([15], 0),
		([16], 0),
		([17], 1),
		([18], 0),
		([19], 1),
		([20], 0),
		([21], 0),
		([22], 0),
		([23], 1),
		([24], 0),
		([25], 0),
		([26], 0),
		([27], 0),
		([28], 0),
		([29], 1),
		([30], 0),
	]),
	
	# Arithmetic functions
	(const(0), [([0], 0), ([9], 0)]),
	(const(1), [([0], 1), ([1], 1), ([3], 1)]),
	(const(2), [([0], 2), ([1], 2), ([2], 2)]),
	(const(3), [([0], 3), ([3], 3), ([5], 3)]),
	
	(pred, [
		([0], 0),
		([1], 0),
		([2], 1),
		([3], 2),
		([9], 8),
	]),
	
	(add, [
		([0, 0], 0),
		([0, 1], 1),
		([0, 3], 3),
		([1, 0], 1),
		([2, 0], 2),
		([1, 1], 2),
		([2, 5], 7),
		([6, 3], 9),
	]),
	
	(sub, [
		([0, 0], 0),
		([0, 1], 0),
		([0, 2], 0),
		([1, 0], 1),
		([1, 1], 0),
		([1, 2], 0),
		([2, 0], 2),
		([2, 1], 1),
		([2, 2], 0),
		([2, 3], 0),
		([3, 0], 3),
		([5, 2], 3),
		([7, 6], 1),
	]),
	
	(subrev, [
		([0, 0], 0),
		([1, 0], 0),
		([2, 0], 0),
		([0, 1], 1),
		([1, 1], 0),
		([2, 1], 0),
		([0, 2], 2),
		([1, 2], 1),
		([2, 2], 0),
		([3, 2], 0),
		([0, 3], 3),
		([2, 5], 3),
		([6, 7], 1),
	]),
	
	(diff, [
		([0, 0], 0),
		([0, 1], 1),
		([0, 2], 2),
		([1, 0], 1),
		([1, 1], 0),
		([1, 2], 1),
		([2, 0], 2),
		([2, 1], 1),
		([2, 2], 0),
		([5, 0], 5),
		([6, 6], 0),
		([3, 7], 4),
	]),
	
	(min, [
		([0, 0], 0),
		([0, 1], 0),
		([0, 2], 0),
		([1, 0], 0),
		([1, 1], 1),
		([1, 2], 1),
		([2, 0], 0),
		([2, 1], 1),
		([2, 2], 2),
		([3, 0], 0),
		([5, 2], 2),
		([7, 6], 6),
	]),
	
	(max, [
		([0, 0], 0),
		([0, 1], 1),
		([0, 2], 2),
		([1, 0], 1),
		([1, 1], 1),
		([1, 2], 2),
		([2, 0], 2),
		([2, 1], 2),
		([2, 2], 2),
		([3, 0], 3),
		([5, 2], 5),
		([7, 6], 7),
	]),
	
	(mul, [
		([0, 0], 0),
		([0, 1], 0),
		([0, 2], 0),
		([1, 0], 0),
		([3, 0], 0),
		([1, 1], 1),
		([1, 2], 2),
		([2, 1], 2),
		([2, 2], 4),
		([3, 7], 21),
		([5, 8], 40),
	]),
	
	(pow, [
		([0, 0],   1),
		([0, 1],   0),
		([0, 2],   0),
		([1, 0],   1),
		([1, 1],   1),
		([1, 2],   1),
		([2, 0],   1),
		([2, 1],   2),
		([2, 2],   4),
		([2, 3],   8),
		([2, 4],  16),
		([2, 5],  32),
		([2, 6],  64),
		([2, 7], 128),
		([2, 8], 256),
		([2, 9], 512),
		([3, 1],   3),
		([3, 2],   9),
		([4, 3],  64),
		([5, 3], 125),
		([6, 2],  36),
	]),
	
	(sqrt, [
		([ 0], 0),
		([ 1], 1),
		([ 2], 1),
		([ 3], 1),
		([ 4], 2),
		([ 5], 2),
		([ 6], 2),
		([ 7], 2),
		([ 8], 2),
		([ 9], 3),
		([10], 3),
		([15], 3),
		([16], 4),
		([17], 4),
		([23], 4),
	]),
	
	(log, [
		([0,  0], 0),
		([0,  1], 1),
		([0,  2], 2),
		([0,  4], 4),
		([0,  7], 7),
		([1,  0], 0),
		([1,  1], 1),
		([1,  2], 2),
		([1,  5], 5),
		([1,  9], 9),
		([2,  0], 0),
		([2,  1], 0),
		([2,  2], 1),
		([2,  3], 1),
		([2,  4], 2),
		([2,  5], 2),
		([2,  6], 2),
		([2,  7], 2),
		([2,  8], 3),
		([2,  9], 3),
		([2, 15], 3),
		([2, 16], 4),
		([2, 17], 4),
		([3,  0], 0),
		([3,  1], 0),
		([3,  2], 0),
		([3,  3], 1),
		([3,  4], 1),
		([3,  8], 1),
		([3,  9], 2),
		([3, 10], 2),
		([3, 26], 2),
		([3, 27], 3),
		([4,  0], 0),
		([4,  1], 0),
		([4,  2], 0),
		([4,  3], 0),
		([4,  4], 1),
		([4,  5], 1),
		([4,  8], 1),
		([4, 15], 1),
		([4, 16], 2),
	]),
	
	(div, [
		([ 0, 0], 0),
		([ 1, 0], 1),
		([ 2, 0], 2),
		([ 3, 0], 3),
		([ 0, 1], 0),
		([ 1, 1], 1),
		([ 2, 1], 2),
		([ 3, 1], 3),
		([ 0, 2], 0),
		([ 1, 2], 0),
		([ 2, 2], 1),
		([ 3, 2], 1),
		([ 4, 2], 2),
		([11, 2], 5),
		([14, 2], 7),
		([ 0, 3], 0),
		([ 1, 3], 0),
		([ 2, 3], 0),
		([ 3, 3], 1),
		([ 4, 3], 1),
		([ 5, 3], 1),
		([ 6, 3], 2),
		([11, 3], 3),
		([18, 3], 6),
		([ 8, 4], 2),
		([ 0, 4], 0),
		([23, 4], 5),
		([20, 5], 4),
		([21, 5], 4),
		([ 5, 6], 0),
		([30, 6], 5),
		([ 2, 7], 0),
		([19, 7], 2),
	]),
	
	(mod, [
		([ 0, 0], 0),
		([ 1, 0], 1),
		([ 2, 0], 2),
		([ 3, 0], 3),
		([ 0, 1], 0),
		([ 1, 1], 0),
		([ 2, 1], 0),
		([ 3, 1], 0),
		([ 0, 2], 0),
		([ 1, 2], 1),
		([ 2, 2], 0),
		([ 3, 2], 1),
		([ 0, 3], 0),
		([ 1, 3], 1),
		([ 2, 3], 2),
		([ 3, 3], 0),
		([ 4, 3], 1),
		([ 5, 3], 2),
		([ 7, 4], 3),
		([21, 5], 1),
		([30, 6], 0),
		([19, 7], 5),
	]),
	
	(factorial, [
		([0],   1),
		([1],   1),
		([2],   2),
		([3],   6),
		([4],  24),
		([5], 120),
		([6], 720),
	]),
	
	(gcd, [
		([ 0,  0],  0),
		([ 0,  1],  1),
		([ 0,  2],  2),
		([ 0,  3],  3),
		([ 1,  0],  1),
		([ 1,  1],  1),
		([ 1,  2],  1),
		([ 1,  3],  1),
		([ 2,  0],  2),
		([ 2,  1],  1),
		([ 2,  2],  2),
		([ 2,  3],  1),
		([ 2,  4],  2),
		([ 3,  0],  3),
		([ 3,  1],  1),
		([ 3,  2],  1),
		([ 3,  3],  3),
		([ 6,  2],  2),
		([ 6,  3],  3),
		([ 6,  6],  6),
		([12,  2],  2),
		([12,  3],  3),
		([12,  4],  4),
		([12,  6],  6),
	]),
	
	(lcm, [
		([ 0,  0],  0),
		([ 0,  1],  0),
		([ 0,  2],  0),
		([ 1,  0],  0),
		([ 1,  1],  1),
		([ 1,  2],  2),
		([ 1,  3],  3),
		([ 2,  0],  0),
		([ 2,  1],  2),
		([ 2,  2],  2),
		([ 2,  3],  6),
		([ 2,  4],  4),
		([ 3,  0],  0),
		([ 3,  1],  3),
		([ 3,  2],  6),
		([ 3,  3],  3),
		([ 3,  5], 15),
		([ 6, 15], 30),
		([ 6, 30], 30),
		([10, 15], 30),
	]),
	
	(divisiblecount, [
		([ 0, 0], 0),
		([ 1, 0], 0),
		([ 2, 0], 0),
		([ 4, 0], 0),
		([ 7, 0], 0),
		([ 0, 1], 0),
		([ 1, 1], 1),
		([ 2, 1], 2),
		([ 5, 1], 5),
		([ 9, 1], 9),
		([ 0, 2], 0),
		([ 1, 2], 0),
		([ 2, 2], 1),
		([ 3, 2], 0),
		([ 4, 2], 2),
		([ 5, 2], 0),
		([ 6, 2], 1),
		([ 7, 2], 0),
		([ 8, 2], 3),
		([ 9, 2], 0),
		([10, 2], 1),
		([ 0, 3], 0),
		([ 1, 3], 0),
		([ 2, 3], 0),
		([ 3, 3], 1),
		([ 4, 3], 0),
		([ 5, 3], 0),
		([ 6, 3], 1),
		([ 7, 3], 0),
		([ 8, 3], 0),
		([ 9, 3], 2),
		([10, 3], 0),
		([ 0, 4], 0),
		([ 3, 4], 0),
		([ 4, 4], 1),
		([ 5, 4], 0),
		([ 8, 4], 1),
		([16, 4], 2),
	]),
	
	(nthprime, [
		([0], 2),
		([1], 3),
		([2], 5),
		([3], 7),
	]),
	
	(fibonacci, [
		([0], 0),
		([1], 1),
		([2], 1),
		([3], 2),
		([4], 3),
		([5], 5),
	]),
	
	# Bitwise functions
	(shl, [
		([0, 0],  0),
		([1, 0],  1),
		([2, 0],  2),
		([3, 0],  3),
		([0, 1],  0),
		([1, 1],  2),
		([2, 1],  4),
		([3, 1],  6),
		([0, 2],  0),
		([1, 2],  4),
		([2, 2],  8),
		([3, 2], 12),
		([0, 3],  0),
		([1, 3],  8),
		([2, 3], 16),
		([3, 3], 24),
	]),
	
	(shr, [
		([0, 0], 0),
		([1, 0], 1),
		([2, 0], 2),
		([3, 0], 3),
		([0, 1], 0),
		([1, 1], 0),
		([2, 1], 1),
		([3, 1], 1),
		([0, 2], 0),
		([1, 2], 0),
		([2, 2], 0),
		([3, 2], 0),
		([4, 2], 1),
		([5, 2], 1),
		([6, 2], 1),
		([7, 2], 1),
		([8, 2], 2),
	]),
	
	(band, [
		([0, 0], 0),
		([1, 0], 0),
		([2, 0], 0),
		([3, 0], 0),
		([0, 1], 0),
		([1, 1], 1),
		([2, 1], 0),
		([3, 1], 1),
		([0, 2], 0),
		([1, 2], 0),
		([2, 2], 2),
		([3, 2], 2),
		([0, 3], 0),
		([1, 3], 1),
		([2, 3], 2),
		([3, 3], 3),
	]),
	
	(bandnot, [
		([0, 0], 0),
		([1, 0], 1),
		([2, 0], 2),
		([3, 0], 3),
		([0, 1], 0),
		([1, 1], 0),
		([2, 1], 2),
		([3, 1], 2),
		([0, 2], 0),
		([1, 2], 1),
		([2, 2], 0),
		([3, 2], 1),
		([0, 3], 0),
		([1, 3], 0),
		([2, 3], 0),
		([3, 3], 0),
	]),
	
	(bor, [
		([0, 0], 0),
		([1, 0], 1),
		([2, 0], 2),
		([3, 0], 3),
		([0, 1], 1),
		([1, 1], 1),
		([2, 1], 3),
		([3, 1], 3),
		([0, 2], 2),
		([1, 2], 3),
		([2, 2], 2),
		([3, 2], 3),
		([0, 3], 3),
		([1, 3], 3),
		([2, 3], 3),
		([3, 3], 3),
	]),
	
	(bxor, [
		([0, 0], 0),
		([1, 0], 1),
		([2, 0], 2),
		([3, 0], 3),
		([0, 1], 1),
		([1, 1], 0),
		([2, 1], 3),
		([3, 1], 2),
		([0, 2], 2),
		([1, 2], 3),
		([2, 2], 0),
		([3, 2], 1),
		([0, 3], 3),
		([1, 3], 2),
		([2, 3], 1),
		([3, 3], 0),
	]),
	
	(getbit, [
		([ 0, 0], 0),
		([ 1, 0], 1),
		([ 2, 0], 0),
		([ 3, 0], 1),
		([ 0, 1], 0),
		([ 1, 1], 0),
		([ 2, 1], 1),
		([ 3, 1], 1),
		([ 0, 2], 0),
		([ 1, 2], 0),
		([ 2, 2], 0),
		([ 3, 2], 0),
		([ 4, 2], 1),
		([ 5, 2], 1),
		([ 6, 2], 1),
		([ 7, 2], 1),
		([ 0, 3], 0),
		([ 5, 3], 0),
		([ 8, 3], 1),
		([ 9, 3], 1),
		([16, 3], 0),
	]),
]


if __name__ == "__main__":
	print("Running tests...")
	count: int = 0
	failed: bool = False
	for (f, cases) in testsuites:  # For each test suite
		for (arg, ans) in cases:   # For each test case
			actual: int = f.eval(arg)
			if actual != ans:
				if not failed:
					print("One or more tests failed:")
					failed = True
				print(f"    {str(f)} {str(arg)} = {str(actual)} != {str(ans)}")
			count += 1
	if not failed:
		print(f"All {count} tests passed")
