import sys
from math import sqrt

def main():
    a = 3
    b = 4
    triplets = []
    for i in range(3,1000):
        for j in range(4,1000):
            if i<j:
                if sqrt(i**2+j**2) == int(sqrt(i**2+j**2)):
                    triplets.append((i,j))
                    if i+j+sqrt(i**2+j**2) == 1000:
                        print (i,j,int(sqrt(i**2+j**2))) 

if __name__=='__main__':
    status = main()
    sys.exit(status)