import matplotlib.pyplot as pt
import numpy as np

pt.rcParams['font.sans-serif']=['SimHei']

one_row=[]

def main():

	target_file = 'climate.txt'
	with open(target_file, 'r', encoding='utf-8') as fp:
		raw_data = fp.readlines()

	for i in raw_data:
		one_row.append(i.rstrip('\n').split('\t'))

def manu():
	cout=0
	for a in one_row:
		if cout % 5 == 0:
			print("{:>2}:{:<6}\t".format(cout,a[0]),end="")
			cout += 1
			print()
		else:
			print("{:>2}:{:<6}\t".format(cout,a[0]),end="")
			cout += 1

	print()

def show_temper():
	a = int(input("輸入你要查詢地區的編碼，輸入-1以結束程式:"))
	if a == -1 :
		return 0

	else:
		month = list()
		temper = list()
		print("你要查詢的地點 :",one_row[a][0])
		print("--------------------------------")
		for i in range(1,13):
			print("{}月份的平均氣溫是 {}".format(i,one_row[a][i]))
			month.append(i)
			temper.append(float(one_row[a][i]))
		print("年均溫為:",one_row[a][13])
		print("--------------------------------")
		ind = np.arange(len(temper))+1
		print(ind)

		pt.barh(ind,temper)
		pt.yticks(ind,month)
		pt.title("Program 02")
		pt.show()

	show_temper()

main()
manu()
show_temper()