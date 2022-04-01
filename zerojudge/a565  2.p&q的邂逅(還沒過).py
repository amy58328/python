n = int(input())


while n:
	str = input()
	count = 0
	q = 0
	p = 0

	for i in str:
		print(i)
		if i == "p":
			p+=1

		elif i == "q" and p>0:
			p-=1
			count+=1

		if i == "\n":
			print(count)
	n-=1

	