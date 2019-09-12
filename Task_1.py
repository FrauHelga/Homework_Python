#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import array

def while_func(list2):
	summ=0
	count=0
	if len(list2)==0:
		return "Empty array. Summ is 0."
		raise ValueError
	else:
		while count<len(list2):
			summ += list2[count]
			count+=1
	return summ

def for_func(list1):
	summ=0
	if len(list1)==0:
		return "Empty array. Summ is 0."
		raise ValueError
	else:
		for i in list1:
			summ+=i
	return summ
	

def recurs_func(list3):
	if len(list3) == 0:
		print("Empty array. Summ is 0.")
		raise ValueError
	if len(list3) == 1:
		return list3[0]
	return list3[0] + recurs_func(list3[1:])


if __name__ == "__main__":

	c=[]
	try:
		op = sys.argv[1]
		for i in range (2,len(sys.argv)):
			c.append(float(sys.argv[i])) 
		if op =='-f':
			print('Summ in for=  ', for_func(c))
		elif op == '-w':
			print('Summ in while=  ', while_func(c))
		elif op == '-r':
			print('Summ in recurs=  ', recurs_func(c))
		else: 
			raise ValueError
	except ValueError:
		print('Некорректный ввод данных')
		exit(1)

	
	