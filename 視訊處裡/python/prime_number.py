def f(a,b):
	L=[]
	t=0
	for i in range(a, int(b+1)):
		cout = 0 
		for j in range(2,i+1):
			if i%j == 0 :
				cout += 1

		if cout == 1 :
			L.append(i)
	return L		


left = int(input())
right = int(input())

answer = f(left,right)
print("{}到{}之間的質數有{}".format(left,right,answer))

