import csv
import matplotlib.pyplot as plt

list1=[]
list2=[]
with open('hell.csv','r') as f:
	r = csv.reader(f, delimiter=',')
	i=0;
	for row in r:
			print(row[/*content index*/])
			
