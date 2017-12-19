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

$$IL =  \Sigma_{j=0}^{n-1} 1 = n$$

$$OL = \Sigma_{i=0}^{n-1} IL = n\times IL = n\times n = n^2$$

$$n^2 \in O(n^2),\Omega(n^2) \to \Theta(n^2)$$

### Example 2

```C
int sum = 0;
    for ( int i = 1; i <= n; i++)
        for ( int j = 0; j < i*i ; j++)
            sum++;
```

$$IL = \Sigma_{j=0}^{i^2} 1 = i^2$$

$$OL =\Sigma_{i=1}^{n} IL = \Sigma_{i=1}^{n} i^2 $$

$$= n \times \frac{(n+1)\times(2n+1)}{6}$$

$$= \frac{1}{6}(2n^3+n^2+2n^2+n) \in \Theta(n^3)$$

### Example 3

```C
for(int i=0; i<n; i++)
    for(int j=0; j<n; j++)
        for(int k=0; k<n; k++)
            sum++;
```

$$IL_A = \Sigma_{k\in n} 1 = n$$

$$IL_B = \Sigma_{j\in n} IL_A = n\times n = n^2$$

$$OL = \Sigma_{i\in n} IL_B = n\times n^2 = n^3$$

$$\to \Theta(n^3)$$

### Example 4

```C
    for (int i = 1 ; i <= n; i*=2 )
        for (int j = 0; j <= n ; j++ )
            sum++;
```

$$IL = \Sigma_{j\in n}1 = n$$$$OL = \Sigma_{i = 1}^{log_{2}n} IL = n * log_2n$$$$\to \Theta(nlogn)$$

### Example 5

```c
for ( i < 1; i < n; i++ )
    if ( n%2 == 0 )
        for ( j = 0; j < n; j++ )
            sum++;
    else
        sum--;
```

$$\Sigma_{i \in n} max\{if_a,if_b\}$$

$$max\{if_a,if_b\} = max\{\Sigma_{j\in n}1,1\} = \Sigma_{j\in n}1 = n$$

$$\Sigma_{i \in n} max\{if_a,if_b\} = \Sigma_{i \in n}n = n^2$$


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

      $\Sigma_{i=0}^{n}1 = n \in O(n)$

  1. *Recursively* search the array for the element and reducing the size of the array each time in half. Like below:
  ![binary_search](../../images/binary-search1.png)
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

File is available [here](../../Code/Algorithms/Arrays/binary_search.py).

Size | Operations
|-|-|
10|4|
100|7
1000|10|
1,000,000|20|
1,000,000,000|30|

In essence, binary search makes 1 operation, the comparison, then lessens the size of available array by half each time until there is only 1 element left. So if we were to start with 1024 elements, after 1 recursion, we would have 512 elements, then 256, 128, 64, 32, 16, 8, 4, 2, 1.

Since we are diving by 2 each time, we have $log_2$. As a result, with 1024 elements, we would have $log_21024$ or 10 operations.

So we conclude that binary search $\in O(log_2n)$

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
$$f(n) = f(n/2)+3$$
The recursive condition is:
$$f(1) = 1$$

Using substitution:
$$T(n) = T(n/2)+3$$

$$=T(n/4)+3 +3$$

$$=T(n/8)+3+3+3$$

$$=T(n/16)+3+3+3+3$$

$$=1+3+.....+3 $$

$$= 1+ 3*log_2n$$

$$= 1+3*log_2n $$

$$\implies T(n)|_{binary\ search} \in O(log_2n)$$

In similar fashion, depending on the size of the segments we reduce our problem to, we have the equivalent logarithmic base.

If I were to split an array each time in segments of $\frac{n}{3}$ the base of the logarithm will be 3.

An exception to this is $\sqrt{n}$. When we split an array of $n$ elements into segments of size $\sqrt{n}$ we have $\sqrt{n}$ segments.

Suppose a sorted list where we can look ahead $\sqrt{n}$ elements. If we were to calculate the insertion runtime, under normal circumstances we would say it's in the order of $O(n)$, but since we can look ahead $\sqrt{n}$ elements, we can check in $O(1)$ if the  $\sqrt{n}_{th}$ element after the current is bigger or smaller than the element we are trying to insert and skip to that. Because we can look ahead $\sqrt{n}$ elements, we essentially split the problem into segments of $\sqrt{n}$. So to insert an element in such list, we have the following operations:

* Find the segment where we will insert the element.
  $\implies = O(\sqrt{n})$
  We treat each element we can look ahead to as an element in an array and the array is of size $\sqrt{n}$ thus $O(\sqrt{n})$ run time.

* Find the position we are trying to insert the element.

  $\implies O(\sqrt{n})$

  Similarly to the previous step, we iterate an array of 

  $\sqrt{n}$ elements thus $O(n)$.

$\implies O(\sqrt{n})+O(\sqrt{n}) = O(2*\sqrt{n}) = O(\sqrt{n})$

This is type of list is called a skiplist and will be given more attention in a later lecture.