# c471: apcs 物品堆疊 (Stacking)

from functools import cmp_to_key

def compare(obj1,obj2):
	return obj1[0] * obj2[1] - obj1[1] * obj2[0]


while True:
	try:
		N = int(input().strip())
		W = input().strip().split()
		F = input().strip().split()

		obj = [[int(W[i]),int(F[i])] for i in range(len(W))]

		obj.sort(key = cmp_to_key(compare))

		energy = 0
		cum_w = 0
		for i in range(N-1):
			cum_w += obj[i][0]
			energy += obj[i+1][1]* cum_w

		print(energy)

	except:
		break