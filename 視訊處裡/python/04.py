import matplotlib.pyplot as pt
import numpy as np

with open('popu.txt', 'r') as fp:
	populations = fp.readlines()

print(populations)

city = list()
popu = list()

for p in populations:
	cc, pp = p.rstrip('\n').split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city)/2)
print(ind)

popu1=[]
city1=[]
lenCity1=int(len(city)/2)
lenCity2=lenCity1

for i in range(lenCity1):
	popu1.append(popu[i])
	city1.append(city[i])

popu2=[]
city2=[]
for i in range(lenCity2):
	popu2.append(popu[lenCity1+i])
	city2.append(city[lenCity1+i])

pt.subplot(121)
pt.bar(ind, popu1)
pt.xticks(ind, city1)
pt.title('city1')

pt.subplot(122)
pt.bar(ind, popu2)
pt.xticks(ind, city2)
pt.title('city2')

pt.show()
