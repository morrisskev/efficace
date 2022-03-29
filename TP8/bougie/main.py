import sys
from time import sleep
from unicodedata import name 
def  somme_age (rith_bj , somme_bji): 
  i = 3 
  j = 4 
  while  (i  + j )  != somme_bji and  somme_bji <=  2000  : 
     i =  i  + i+1
     j =  j + j + 1
    
  
def start() :   
    file = sys.argv[1]
    fs =  open(file) 
    lines  =  fs.read()
    fs.close()
    info =  lines.split() 
    info = [int(ele) for  ele  in  info ]
    diff_age  =  info[0]
    ritha_bj  =  info[1]
    theo_bj  =  info [2]
    
    
    ritha_age  =  3 +  diff_age 
    theo_age  =  3  
    n_r =  0 

    for  i  in range (4,  ritha_age+1) : 
         n_r  +=  i 

    n_t = 0  

    for  i in range (3,  theo_age+1) : 
         n_t += i 
    
    while  n_r +  n_t  != ritha_bj + theo_bj  : 
        ritha_age +=1 
        theo_age  +=1
        n_r += ritha_age
        n_t += theo_age 

    print ((ritha_bj - n_r))


start()    




