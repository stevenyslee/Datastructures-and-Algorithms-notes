# Lecture 4 Building Datastructures using LinkedLists
___
__Table of Contents__

1. [LinkedLists](#linked-lists)
    1. Python implementation
    2. C implementation
    2. Stacks
        3. Python implementation
        3. C implementation
    2. Queues
        3. Python implementation
        3. C implementation
1. Usage examples
    2. Stack
    2. Queue


___

##Linked Lists
    
A linked list is a sequence of nodes. The simplest form of a linked list has two ( 2 ) fields:
  
a. A `pointer` to the `next` node.
b. A `pointer` to the `current` element in the list.

|Simple Linked-List|Array-List| Operation |
|-----------|----------|:---------:|
|$\Theta(1)$| $O(n)$*, $\Omega$(1)| `Insert`, `Append` first / last element|
|$O(n)$     | $O(1)$   | Random element access |
|$O(n)$     | $O(n)$   | Search for element |
|$O(n)$**     | $O(n)$   | Space|


\* Insertion on the ends depends on the implementation, it is possible for $O(1)$ `insert` and `append` but needs slightly more sophistication than the obvious array list implementations. For reference, Python's built-in list is an arrayList with $O(1)$ append and insert.


\*\* Simple LinkedLists require double the space compared to arrays due to the 2 ( two ) pointer fields of each node.

```

```