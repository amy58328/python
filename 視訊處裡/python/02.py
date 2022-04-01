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

ind = np.arange(len(city))
print(ind)

pt.bar(ind, popu)
pt.xticks(ind, city)
pt.title('Program 02')
pt.show()
