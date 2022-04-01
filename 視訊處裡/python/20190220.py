import random

a = random.randint(0,99)
print(a)
l = 0
r = 99
time = 0
while True :
	print("Please enter a number between" , l , "and" , r , ":")
	b = input()
	b = int(b)
	if b > a :
		print("\nThe number is too large.")
		r = b-1
		time += 1

	if b < a :
		print("\nThe number is too small.")
		l = b+1
		time += 1

	if b == a :
		print("\nyou win")
		print("the time you guess is :",time)
		break


