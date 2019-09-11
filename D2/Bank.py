#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def bank (a, years):
	money=0
	if a>100 and years>0 and years<21:
		money = a
		for i in range (years):
			money = money + (money * 0.1)
			print (money-a)
		return money
	else:
		return 'Некорректные данные'

if __name__ == "__main__":
	
	if len(sys.argv) != 3:
		print("Недостаточно параметров")
		exit(1)
	
	try:
		a,b =float(sys.argv[1]), int(sys.argv[2])
		print (bank(a, b))
	except ValueError:
		print('Некорректный ввод данных')
		exit(1)
	