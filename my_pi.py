#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# https://en.wikipedia.org/wiki/Chudnovsky_algorithm


from decimal import Decimal, getcontext
from math import factorial
import sys

def calculate_pi(max_K, number_of_digits):
	getcontext.prec = number_of_digits+2
	a_k, b_k, C, a_sum, b_sum  =  1, 0, 640320, 1, 0
	for k in range(1,max_K):
		a_k *= -(Decimal(24)/Decimal(C**3))*Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k**3)
		a_sum += a_k
		b_sum += a_k*k


	pi = 426880*Decimal(10005).sqrt()/Decimal(13591409*a_sum + 545140134*b_sum)
	print str(pi)[:number_of_digits+2]

def main(number_of_digits):
	pi = calculate_pi(10000, number_of_digits)


if __name__ == "__main__":
	number_of_digits = int(sys.argv[1])
	main(number_of_digits)