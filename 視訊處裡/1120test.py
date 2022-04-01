import re
import linecache
import numpy as np
import os

# filename = 'input.txt'
f = 'input.txt'

w = np.array([
	[1,0],
	[0,1]
])

print(w)

b = np.array([
	[1],
	[1]
])

print(b)

# p = np.array([
# 	[1],
# 	[1]
# ])

# print(p)

# a = w.dot(p) + p

# print(a)


# ele = []
# with open(filename) as file:
# 	for line in file:
# 		line = line.strip().split()
# 		ele.append(line)

# ele_array = np.array(ele)
# print(ele_array)

# for e in ele_array:
# 	e = np.array(e)	
# 	a = w.dot(e)+p
# 	print(a)


file=open('input.txt')
lines=file.readlines()
#print lines
#['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']形式
rows=len(lines)#檔案行數

datamat=np.zeros((rows,8),dtype = float)#初始化矩陣

row=0
for line in lines:
    line=line.strip().split('\t')#strip()預設移除字串首尾空格或換行符
    line = float(line)
    datamat[row,:]=line[:]
    row+=1




