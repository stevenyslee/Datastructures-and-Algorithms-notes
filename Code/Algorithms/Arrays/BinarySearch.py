import random

# Nonpythonic


def pythonic_bs(l,key):

    if len (l) == 1:
        return l[0] == key
    if  l[len(l) // 2] <= key:
        return pythonic_bs(l[len(l)//2:],key)
    return pythonic_bs(l[:len(l)//2],key)

def bs(l, x, low, high):

    if high-low <= 1:
        return l[low] == x
    
    mid = (low+high)//2
    
    if l[mid] == x:
        return True
    if l[mid]>= x:
        return bs(l,x,low,mid)
    return bs(l,x,mid,high)

l = [x for x in range(100)]


u = sorted(set([int(random.random() * 1000) for x in range(200)]))

for x in range(-1000,1000):
    res = x in u
    assert res == pythonic_bs(u,x) 
    assert res == bs(u,x,0,len(u))

