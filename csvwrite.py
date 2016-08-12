import csv
def read_file():
    with open('hell.csv', 'w') as f:
        with open('hell.csv','a') as f:
    	   w=csv.writer(f)
    	   first =raw_input("enter the first heading\n")
    	   second =raw_input("enter the second heading\n")
    	   mark11=raw_input("enter the third heading\n")
    	   mark22=raw_input("enter the fourth heading\n")
    	   w.writerow([first,second,mark11,mark22])
         
    n =int( raw_input("enter the no of student\n"))
    for i in range(n):
    	first =raw_input("enter the first\n")
    	second =raw_input("enter the second\n")
    	mark1=int( raw_input("enter the mark1\n"))
    	mark2=int( raw_input("enter the mark2\n"))
    	with open('hell.csv','a') as f:
    	   w=csv.writer(f)
    	   l=i+2;
    	   e=str(l);
    	   w.writerow([first,second,mark1,mark2])
    	f.close()
	
    return;
