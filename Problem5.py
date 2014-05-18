import sys

def main():
    smallest = 1
    factors = []
    for i in range(1,21):
        if smallest % i == 0:
            factors.append(1)
        else:
            m = i
            divides = False
            for j in factors:
                if (m % j == 0):
                    divides = True
                    m = m / j
            if divides:
                smallest *= m
                factors.append(m)
            else:
                smallest*=i
                factors.append(i)
                
    print smallest
    print factors
    print range(1,21)
    
if __name__=='__main__':
    status = main()
    sys.exit(status)