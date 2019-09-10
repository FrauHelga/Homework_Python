#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

def square(side):
	if side > 0:
		pe = 4 * side
		sq = side ** 2
		di = side * (math.sqrt(2))
		return pe, sq, di
	else:
		print ('Введите число больше 0')
		exit(1)

if __name__ == "__main__":
	
	if len(sys.argv) == 2:
		try:
			a =float(sys.argv[1])
			print ('Perimetr: {0[0]}, Sqare: {0[1]}, Diagonal: {0[2]}'.format(square(a)))
		except ValueError:
			print('Некорректный ввод данных')
			exit(1)
	else:
		print('Введите только число')
		exit(1)