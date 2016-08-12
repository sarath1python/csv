//here hell is the csv file present
import csv
import matplotlib.pyplot as plt

list1=[]
list2=[]
with open('hell.csv','r') as f:
	r = csv.reader(f, delimiter=',')
	i=0;
	for row in r:
		if i>0:
			list1.append(row[2])
			list2.append(row[3])
		else:
			mark1=row[2]
			mark2=row[3]
		i=i+1
plt.plot(list1,list2,'r-')
plt.ylabel('mark1')
plt.xlabel('mark2')
plt.show()
