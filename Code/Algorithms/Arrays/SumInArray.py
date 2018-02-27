
##
# Sum lookup in an array using 3 methods
#  i)    A naive approach that includes all combinations with O (n^2).
#  ii)   A less naive approach where the array is sorted and then looked through with:
#        O(nlogn +n) => O(nlogn) time complexity.This method can't find the index of the
#        items,only the existance of a pair, with some modifications it's easy to find it
#  iii)  A Map approach where the array[i] is looked into a map as a key, if it exists then
#        the pair is found, otherwise we insert 
#        O(n) time complexity



import random as rand
from time import time


def naive(array, sum):
   for i, x in enumerate(array[0:]):
      for j, y in enumerate(array[i:]):
         if x + y == sum:
            return (i,i+j)


def quick(array, sum):
   p = sorted(array)
   i = 0
   j = len(p) - 1

   while i != j:
	   
      if p[i] + p[j] < sum:
         i += 1
      if p[i] + p[j] > sum:
         j -= 1

      if p[i] + p[j] == sum:
         return "Sort result: "+str(p[i])+" + "+str(p[j]) + " = " +str(p[i]+p[j])
        

def mapped(array, sum):
   o = dict()

   for i, value in enumerate(array):
      if value in o:
         return (i,o.get(value))
      else:
         o[sum - value] = i


upper_bound = 1000000
rnge = 20000
u = [int(rand.random()*upper_bound) for x in range(rnge)]

i = int(rand.random()*rnge)
j = int(rand.random()*rnge)
val = u[i]+u[j]
 
o = time()
naive_result = naive(u, val)
t = time()
naive_time = int((t-o)*1000)


o = time()
sort_result = quick(u, val)
t = time()
sort_time = int((t-o)*1000)

o = time()
mapped_result = mapped(u, val)
t = time()
map_time = int((t-o)*1000)

print("Naive result: "+str(u[naive_result[0]])+ " + " + str(u[naive_result[1]]) + " = "+str( u[naive_result[0]] + u[naive_result[1]]) )
print(sort_result)
print("Map result: "+str(u[mapped_result[0]])+ " + " + str(u[mapped_result[1]]) + " = "+str(u[mapped_result[0]] + u[mapped_result[1]]) )
print("naive time:",naive_time,"ms, sort time:",sort_time,"ms, map time",map_time,"ms")
