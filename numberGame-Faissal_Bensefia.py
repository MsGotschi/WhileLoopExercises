#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################LICENCE####################################
#Copyright (c) 2016 Faissal Bensefia
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
################################################################################
# Date:
#  7/10/2016
# Description:
#  Horribly written while loop exercises.
import random
lastCh=""
while lastCh.lower()!="x":
	lastCh=input("Enter a character: ")[:1]
total=0
while total<100:
	total+=int(input("Enter a number: "))

while True:
	num=random.randrange(1,100)
	attempts=0
	while attempts<6:
		guess=int(input("[Attempts remaining "+str(6-attempts)+"] Guess the number between 1 & 100: "))
		print(["Too large!","Correct!","Too small!"][((num>guess)-(num<guess))+1])
		if guess==num:
			break
		else:
			attempts+=1
			if attempts>=6:
				print("The number was "+str(num))
				break
