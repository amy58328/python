for i in range(1,10) :
	for j in range(1,10) :
		print(i, "*" , j , "=" ,i*j)

	print()

for i in range(1,11):
	print("+",end='')

print("\n")

for i in range(1,10) :
	for j in range(1,10) :
		print(i, "*" , j , "=" ,i*j,end='')
		if i*j >= 10 :
			print(end = ' ')
		if i*j < 10 :
			print(end = '  ')

	print()


print("\n")


for q in range(0,3) :
	n = 1 + 3*q
	m = 3 + 3*q
	for i in range(1,10) :
		for j in range(n,m+1) :
			print(j, "*" , i , "=" ,i*j ,end = ' ')
			if i*j < 10 :
				print(end=' ')

		print()
	print()
