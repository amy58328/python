

while True:
	n = int(input())

	if n == 0:
		break

	discarded = []
	lis = []

	for i in range(1,n+1):
		lis.append(i)

	while len(lis) > 1:
		discarded.append(lis.pop(0))
		lis.append(lis.pop(0))

	print("Discarded cards:",", ".join(str(c) for c in discarded))
	print('Remaining card:',lis[0])