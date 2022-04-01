import numpy as np
import random
import matplotlib.pyplot as plt

a = []
x = []
num = []
data_ave = []


# 初始num[]
for i in range(0,31):
	num.append(0)
	data_ave.append(0)
	x.append(i+130)

# 生成10萬筆資料 並記錄身高的個數
for i in range(0,100000):
	b = random.randint(130,160)
	a.append(b)
	b -= 130
	num[b] += 1

# 輸出長條圖
plt.bar(x,num)
plt.show()

# 隨機生成 測試的組數
group_num = random.randint(100,250)



for i in range(0,group_num):
	# 隨機生成 測試的資料數量
	data_num = random.randint(10,80)
	height_sum = 0
	# 隨機選取十萬筆中的資料
	for j in range(0,data_num):
		height_sum += a[random.randint(0,100000)]

	ave = height_sum / data_num
	ave -= 130
	data_ave[int(ave)] += 1

plt.bar(x,data_ave)
plt.show()