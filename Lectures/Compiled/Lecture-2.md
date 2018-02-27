# Lecture 2
  
  
---
  
## Nested Loops
  
  
### Example 1
  
  
```C
int sum = 0;
for (int i = 0; i <= n; i++)
    for (int j = 0; j <= n; j++)
        sum++;
```
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IL%20=%20%20&#x5C;Sigma_{j=0}^{n-1}%201%20=%20n"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?OL%20=%20&#x5C;Sigma_{i=0}^{n-1}%20IL%20=%20n&#x5C;times%20IL%20=%20n&#x5C;times%20n%20=%20n^2"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?n^2%20&#x5C;in%20O(n^2),&#x5C;Omega(n^2)%20&#x5C;to%20&#x5C;Theta(n^2)"/></p>  
  
  
### Example 2
  
  
```C
int sum = 0;
    for ( int i = 1; i <= n; i++)
        for ( int j = 0; j < i*i ; j++)
            sum++;
```
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IL%20=%20&#x5C;Sigma_{j=0}^{i^2}%201%20=%20i^2"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?OL%20=&#x5C;Sigma_{i=1}^{n}%20IL%20=%20&#x5C;Sigma_{i=1}^{n}%20i^2"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=%20n%20&#x5C;times%20&#x5C;frac{(n+1)&#x5C;times(2n+1)}{6}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=%20&#x5C;frac{1}{6}(2n^3+n^2+2n^2+n)%20&#x5C;in%20&#x5C;Theta(n^3)"/></p>  
  
  
### Example 3
  
  
```C
for(int i=0; i<n; i++)
    for(int j=0; j<n; j++)
        for(int k=0; k<n; k++)
            sum++;
```
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IL_A%20=%20&#x5C;Sigma_{k&#x5C;in%20n}%201%20=%20n"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IL_B%20=%20&#x5C;Sigma_{j&#x5C;in%20n}%20IL_A%20=%20n&#x5C;times%20n%20=%20n^2"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?OL%20=%20&#x5C;Sigma_{i&#x5C;in%20n}%20IL_B%20=%20n&#x5C;times%20n^2%20=%20n^3"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;to%20&#x5C;Theta(n^3)"/></p>  
  
  
### Example 4
  
  
```C
    for (int i = 1 ; i <= n; i*=2 )
        for (int j = 0; j <= n ; j++ )
            sum++;
```
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IL%20=%20&#x5C;Sigma_{j&#x5C;in%20n}1%20=%20n"/></p>  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?OL%20=%20&#x5C;Sigma_{i%20=%201}^{log_{2}n}%20IL%20=%20n%20*%20log_2n"/></p>  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;to%20&#x5C;Theta(nlogn)"/></p>  
  
  
### Example 5
  
  
```c
for ( i < 1; i < n; i++ )
    if ( n%2 == 0 )
        for ( j = 0; j < n; j++ )
            sum++;
    else
        sum--;
```
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i%20&#x5C;in%20n}%20max&#x5C;{if_a,if_b&#x5C;}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?max&#x5C;{if_a,if_b&#x5C;}%20=%20max&#x5C;{&#x5C;Sigma_{j&#x5C;in%20n}1,1&#x5C;}%20=%20&#x5C;Sigma_{j&#x5C;in%20n}1%20=%20n"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i%20&#x5C;in%20n}%20max&#x5C;{if_a,if_b&#x5C;}%20=%20&#x5C;Sigma_{i%20&#x5C;in%20n}n%20=%20n^2"/></p>  
  
  
### Examples 6-7 : Recursive search for element in a sorted array
  
  
Suppose a sorted array 'A' where we search for element with value 'k'. We can:
  
  1. Iterate over the list as in previous example
      ```C
      int rlinear( int[] elements, int size, int k, int current_pos){
  
            if (current_pos == size) return -1;
  
            if (elements[pos] == k) return pos;
  
            if (elements[pos] > k) return -1;
  
        return rlinear( X, n, k, pos+1);
      }
      ```
      __Worst case__: When K is not in the array and is bigger than all elements.
  
      <img src="https://latex.codecogs.com/gif.latex?&#x5C;Sigma_{i=0}^{n}1%20=%20n%20&#x5C;in%20O(n)"/>
  
  1. *Recursively* search the array for the element and reducing the size of the array each time in half. Like below:
  ![binary_search](../../images/binary-search1.png )
  This is called binary search.
  
  ```python
    ## This is more "pythonic"  version of 
    ## binary search. The algorithm below is closer to
    ## The equivalent code of most programming languages
    ## l -> list of elements
    ## key -> key we are searching for.
    def pythonic_bs(l,key):
        if len (l) == 1:
            return l[0] == key
  
        ## If the middle element is smaller we will search in
        ## a sublist that begins with that element and
        ## goes towards the end
        if  l[len(l) // 2] <= key:
            return pythonic_bs(l[len(l)//2:],key)
        ## otherwise, we will search in a sublist that
        ## ends with the middle element.
        return pythonic_bs(l[:len(l)//2],key)
  
    ## This is more standard way to write a binary
    ## search but is a bit bigger on the code.
    ## l is the list,
    ## X the value we are searching for
    ## low the lower end of the sub array
    ## high the high end of the sub array
    def bs(l, x, low, high):
  
        ## Recursive condition that we reached the
        ## last element.
        if high-low <= 1:
            return l[low] == x
        ## Index of middle value.
        mid = (low+high)//2
        ## Checking the middle element.
        if l[mid] == x:
            return True
        ## Recursive call with upper limit the middle
        if l[mid] > x:
            return bs(l,x,low,mid)
        ## Recursive call with lower limit the middle
        return bs(l,x,mid,high)
 ```
  
File is available [here](../../Code/Algorithms/Arrays/BinarySearch.py )).
  
Size | Operations
|-|-|
10|4|
100|7
1000|10|
1,000,000|20|
1,000,000,000|30|
  
In essence, binary search makes 1 operation, the comparison, then lessens the size of available array by half each time until there is only 1 element left. So if we were to start with 1024 elements, after 1 recursion, we would have 512 elements, then 256, 128, 64, 32, 16, 8, 4, 2, 1.
  
Since we are diving by 2 each time, we have <img src="https://latex.codecogs.com/gif.latex?log_2"/>. As a result, with 1024 elements, we would have <img src="https://latex.codecogs.com/gif.latex?log_21024"/> or 10 operations.
  
So we conclude that binary search <img src="https://latex.codecogs.com/gif.latex?&#x5C;in%20O(log_2n)"/>
  
## Analysing binary search a bit deeper
  
  
```python
    def pythonic_bs(l,key):
        if len (l) == 1:
            return l[0] == key
  
        ## If the middle element is smaller we will search in
        ## a sublist that begins with that element and
        ## goes towards the end
        if  l[len(l) // 2] <= key:
            return pythonic_bs(l[len(l)//2:],key)
        ## otherwise, we will search in a sublist that
        ## ends with the middle element.
        return pythonic_bs(l[:len(l)//2],key)
```
  
The function has 3 operations:
  
* ```if len (l) == 1```
* ```pivot = len(l)//2```
* ```if  l[:pivot][0] <= key```
  
The recursive function is:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?f(n)%20=%20f(n&#x2F;2)+3"/></p>  
  
The recursive condition is:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?f(1)%20=%201"/></p>  
  
  
Using substitution:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?T(n)%20=%20T(n&#x2F;2)+3"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=T(n&#x2F;4)+3%20+3"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=T(n&#x2F;8)+3+3+3"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=T(n&#x2F;16)+3+3+3+3"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=1+3+.....+3"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=%201+%203*log_2n"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=%201+3*log_2n"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;implies%20T(n)|_{binary&#x5C;%20search}%20&#x5C;in%20O(log_2n)"/></p>  
  
  
In similar fashion, depending on the size of the segments we reduce our problem to, we have the equivalent logarithmic base.
  
If I were to split an array each time in segments of <img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{n}{3}"/> the base of the logarithm will be 3.
  
An exception to this is <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/>. When we split an array of <img src="https://latex.codecogs.com/gif.latex?n"/> elements into segments of size <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> we have <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> segments.
  
Suppose a sorted list where we can look ahead <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> elements. If we were to calculate the insertion runtime, under normal circumstances we would say it's in the order of <img src="https://latex.codecogs.com/gif.latex?O(n)"/>, but since we can look ahead <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> elements, we can check in <img src="https://latex.codecogs.com/gif.latex?O(1)"/> if the  <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}_{th}"/> element after the current is bigger or smaller than the element we are trying to insert and skip to that. Because we can look ahead <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> elements, we essentially split the problem into segments of <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/>. So to insert an element in such list, we have the following operations:
  
* Find the segment where we will insert the element.
  <img src="https://latex.codecogs.com/gif.latex?&#x5C;implies%20=%20O(&#x5C;sqrt{n})"/>
  We treat each element we can look ahead to as an element in an array and the array is of size <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> thus <img src="https://latex.codecogs.com/gif.latex?O(&#x5C;sqrt{n})"/> run time.
  
* Find the position we are trying to insert the element.
  
  <img src="https://latex.codecogs.com/gif.latex?&#x5C;implies%20O(&#x5C;sqrt{n})"/>
  
  Similarly to the previous step, we iterate an array of 
  
  <img src="https://latex.codecogs.com/gif.latex?&#x5C;sqrt{n}"/> elements thus <img src="https://latex.codecogs.com/gif.latex?O(n)"/>.
  
<img src="https://latex.codecogs.com/gif.latex?&#x5C;implies%20O(&#x5C;sqrt{n})+O(&#x5C;sqrt{n})%20=%20O(2*&#x5C;sqrt{n})%20=%20O(&#x5C;sqrt{n})"/>
  
This is type of list is called a skip-list and will be given more attention in a later lecture.
  