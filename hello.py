#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def abc(*bb):
	xx=0
	for n in bb:
		xx = xx + n
	return xx
nums = [1,2,3]
print (abc(*nums))