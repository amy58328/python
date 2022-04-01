#試試看list 陣列

d={}
d[0]=0
d[1]=1
def dd(n):
	if n==0 or n==1 :
		return n
	if n in d.keys():
		return d[n]
	else :
		d[n] = dd(n-1) + dd(n-2)
		return d[n]

a = int(input())
answer = dd(a)
print(answer)