of = open("bump1.txt","r")
mes = of.readlines() #有加s是一次讀近來 沒加是一次一行

# print(len(mes)) #the number of row
# print(len(mes[0])) # the number of colmns

for i in range(0,len(mes[0])):
	for j in range(0,len(mes)):
		print(mes[j][i],end='')
	print() 