#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def is_prime(number):
	if number >= 0 and number <=1000000:
		if number ==  1:
			return 'True'
		else:
			d = 2
   			while number % d != 0:
   				d = d+1
   			return d == number
	else:
		print ('Введите число от 1 до 1000000')
		exit(1)

if __name__ == "__main__":
	
	if len(sys.argv) == 2:
		try:
			a =int(sys.argv[1])
			print(is_prime(a))
		except ValueError:
			print('Некорректный ввод данных')
			exit(1)
	else:
		print('Введите только число')
		exit(1)