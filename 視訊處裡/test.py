file = open("test.txt","r")
mes = file.readlines()

name = []
minute = []
second = []

for i in range(0,len(mes)):
	name.append(mes[i].split("/")[0])
	minute.append(mes[i].split("/")[1])
	second.append(mes[i].split("/")[2])
	
for i in range(0,len(second)-1):
	for j in range(i+1,len(second)):
		if minute[i] == minute[j]:
			if second[i] > second[j]:
				name[i] ,name[j] = name[j] , name[i]
				minute[i] , minute[j] = minute[j] , minute[i]
				second[i] , second[j] = second[j] , second[i]
		if minute[i] > minute[j]:
			name[i] ,name[j] = name[j] , name[i]
			minute[i] , minute[j] = minute[j] , minute[i]
			second[i] , second[j] = second[j] , second[i]

file = open("text.txt","w")

for i in range(0,len(minute)):
	print(name[i] + " " +minute[i] +":" + second[i],end= "")
	file.write(name[i] + "/" +minute[i] +"/" + second[i])

	
name.clear()
minute.clear()
second.clear()