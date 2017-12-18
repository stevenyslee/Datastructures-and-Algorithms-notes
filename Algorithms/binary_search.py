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

for x in range(-10,110):
    print(x,x in l,bs(l,x,0,100),pythonic_bs(l,x))
