import sys

def check_palindrome(num):
    snum = str(num)
    return snum == snum[::-1]

def main():
    x = range(100,1000)
    y = range(100,1000)
    m = (0,0,0)
    for i in x:
        for j in y:
            if check_palindrome(i*j):
                if m[2]<i*j:
                    m = (i,j,i*j)
    print m
            
    
if __name__=='__main__':
    status = main()
    sys.exit(status)