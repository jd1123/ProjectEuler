import sys

def product(l):
    p = 1
    for i in l:
        p *= i
    return p

def transpose(m):
    return zip(*m)

def check_inline(mat):
    m = 0
    for i in range(0,len(mat)):
        for j in range(0, len(mat[0])-3):
            l = mat[i][j:j+4]
            if product(l) > m:
                m = product(l)
    return m

def check_updown(mat):
    return check_inline(transpose(mat))

# this is not done - only checks diags one way - 
# I want to transform the matrix and run this same operation. I 
# need to think about how to transform it so it will work
# and I don't have to mess with the indicies
def check_diag(mat):
    m = 0
    for rowoffset in range(0,len(mat[0])-3):
        for coloffset in range(0,len(mat)-3):
            l = [mat[rowoffset+i][coloffset+i] for i in range(0,4)]
            if product(l)>m:
                m = product(l)
    return m


def main():
    mat = []
    with open('Problem11.txt') as f:
        for i in f.readlines():
            x = [int(j) for j in i.split(' ')]
            mat.append(x)
    results = []
    results.append(check_inline(mat))
    results.append(check_updown(mat))
    results.append(check_diag(mat))
    print results

    


if __name__=='__main__':
    status = main()
    sys.exit(status)