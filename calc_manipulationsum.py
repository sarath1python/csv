# csv

import csv
import matplotlib.pyplot as plt

list1=[]
list2=[]
def read_file():
    with open('hell.csv', 'w') as f:
        with open('hell.csv','a') as f:
    	   w=csv.writer(f)
    	   first =raw_input("enter the first heading\n")
    	   second =raw_input("enter the second heading\n")
    	   mark11=raw_input("enter the third heading\n")
    	   mark22=raw_input("enter the fourth heading\n")
    	   exp='SUM'
    	   w.writerow([first,second,mark11,mark22,exp])
         
    n =int( raw_input("enter the no of student\n"))
    for i in range(n):
    	first =raw_input("enter the first\n")
    	second =raw_input("enter the second\n")
    	mark1=int( raw_input("enter the mark1\n"))
    	list1.append(mark1)
    	mark2=int( raw_input("enter the mark2\n"))
    	list2.append(mark2)
    	with open('hell.csv','a') as f:
    	   w=csv.writer(f)
    	   l=i+2;
    	   e=str(l);
    	   w.writerow([first,second,mark1,mark2,'=SUM('+chr(67)+e+','+chr(68)+e+')'])
    	f.close()
	
    return;

