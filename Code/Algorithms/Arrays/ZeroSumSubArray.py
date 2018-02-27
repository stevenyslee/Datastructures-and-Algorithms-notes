def naive(array):
   for i, val in enumerate(array):
      sum = 0
      for j, x in enumerate(array[i:]):
         sum+=x
         if sum == 0:
            print(array[i:i+j+1])

def mapping(array):
   mp = dict()
   sum = 0;
   for index,val in enumerate(array):
      sum+=val
      if sum in mp:
         print( array[mp[sum]:index+1])
         mp[sum] = index
      else:
         mp[sum] = index +1

naive([4,2,-3,-1,0,4])
mapping([4,2,-3,-1,0,4])