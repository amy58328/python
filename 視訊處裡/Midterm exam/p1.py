import matplotlib.pyplot as pt
import numpy as np

with open('ExamData.txt', 'r') as fp:
	input_number = fp.readlines()


num = list()

for p in input_number:
	nn = p.rstrip('\n').split(" ")[0]
	nn = int(nn)
	num.append(nn)
	nn = p.rstrip('\n').split(" ")[1]
	nn = int(nn)
	num.append(nn)
	nn = p.rstrip('\n').split(" ")[2]
	nn = int(nn)
	num.append(nn)
	nn = p.rstrip('\n').split(" ")[3]
	nn = int(nn)
	num.append(nn)

sume = 0
for i in range(0,len(num)):
	sume += num[i]

print("Q1-------------------------------")
print(sume)

sume = 0
ss_list = list()

print("Q2-------------------------------")
for i in range(0,len(num)):
	if i!=0 and i%4 == 3:
		sume += num[i]
		print(sume)
		ss_list.append(sume)
		sume = 0
	else :
		sume += num[i]
line_list_ = list()
for i in range(1,9):
	line_list_.append(i)


aa = 0
bb = 0
cc = 0
dd = 0

for i in range(0,len(num)):
	if i % 4 == 0:
		aa += num[i]	
	elif i % 4 == 1:
		bb += num[i]
	elif i % 4 == 2:
		cc += num[i]
	elif i % 4 == 3:
		dd += num[i]
sume_list = list()
sume_list.append(aa)
sume_list.append(bb)
sume_list.append(cc)
sume_list.append(dd)

line_list = list()
for i in range(1,9):
	line_list.append(i)

print(aa)
print(bb)
print(cc)
print(dd)
aa=0
bb=0
cc=0
dd=0
print("Q4-------------------------------")
for i in range(0,4):
	aa += num[i] * num[4+i]
	

for i in range(8,12):
	cc += num[i] * num[4+i]



print(aa+cc)

A = list()
B = list()
C = list()

for i in range(0,len(num)):
	if i <= 15 :
		A.append(num[i])
	else:
		B.append(num[i])

qq = 0
en = 0
for i in range(0,len(A)):
	if i % 4 == 0 :
		qq += A[i] * B[0]

	elif i % 4 == 1:
		qq += A[i] * B[1]
	elif i % 4 == 2:
		qq += A[i] * B[2]
	elif i % 4 == 3:
		qq += A[i] * B[3]
		en = 1
	if en == 1:
		C.append(qq)
		qq = 0
		en = 0

qq = 0
en = 0
for i in range(0,len(A)):
	if i % 4 == 0 :
		qq += A[i] * B[4]

	elif i % 4 == 1:
		qq += A[i] * B[5]
	elif i % 4 == 2:
		qq += A[i] * B[6]
	elif i % 4 == 3:
		qq += A[i] * B[7]
		en = 1
	if en == 1:
		C.append(qq)
		qq = 0
		en = 0

qq = 0
en = 0
for i in range(0,len(A)):
	if i % 4 == 0 :
		qq += A[i] * B[8]

	elif i % 4 == 1:
		qq += A[i] * B[9]
	elif i % 4 == 2:
		qq += A[i] * B[10]
	elif i % 4 == 3:
		qq += A[i] * B[11]
		en = 1
	if en == 1:
		C.append(qq)
		qq = 0
		en = 0

qq = 0
en = 0
for i in range(0,len(A)):
	if i % 4 == 0 :
		qq += A[i] * B[12]

	elif i % 4 == 1:
		qq += A[i] * B[13]
	elif i % 4 == 2:
		qq += A[i] * B[14]
	elif i % 4 == 3:
		qq += A[i] * B[15]
		en = 1
	if en == 1:
		C.append(qq)
		qq = 0
		en = 0

print("Q5-------------------------------")
for i in range(0,len(C)):
	if i % 4 == 0:
		print(C[i] ,end = " ")
print()

for i in range(0,len(C)):
	if i % 4 == 1:
		print(C[i] ,end = " ")
print()

for i in range(0,len(C)):
	if i % 4 == 2:
		print(C[i] ,end = " ")
print()

for i in range(0,len(C)):
	if i % 4 == 3:
		print(C[i] ,end = " ")
print()


ind = np.arange(len(ss_list))+1
pt.subplot(211)
pt.barh(ind, ss_list)
pt.yticks(ind, line_list_)
pt.title('test')

ind = np.arange(len(sume_list))*2
pt.subplot(212)
pt.bar(ind, sume_list)
pt.xticks(ind, line_list)
pt.title('test')
pt.show()
