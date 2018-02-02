
import random

debug = False 

def makeu():
    numbits = random.randrange(3, 12)
    zlsb = random.randrange(0, numbits)
    zmsb = random.randrange(zlsb, numbits)
    n = (1 << numbits) - 1
    n ^= (1 << zmsb) - 1
    n ^= (1 << zlsb) - 1
    if debug: 
        print "%s, %#x, %#o, %s" % (format(n, "#b"), n, n, (numbits, zmsb, zlsb))
    return n


for i in range(20):
    formatChar = "xo"[i%2]
    formatStr = "%%#%c" % formatChar
    print formatStr % makeu()
