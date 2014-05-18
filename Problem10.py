import sys
from Problem7 import isprime

def main():
    s = 0
    for i in range(2, 2000001):
        if isprime(i):
            s+=i
    print s

if __name__=='__main__':
    status = main()
    sys.exit(status)