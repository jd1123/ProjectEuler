import sys

def sumofsquares(rng):
    sum = 0
    for r in rng:
        sum+=r*r
    return sum

def squareofsum(rng):
    sum = 0
    for r in rng:
        sum+=r
    return sum*sum

def main():
    rng = range(1,101)
    print squareofsum(rng) - sumofsquares(rng) 
    
if __name__=='__main__':
    status = main()
    sys.exit(status)