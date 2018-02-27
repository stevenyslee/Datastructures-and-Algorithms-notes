class Node:

    def __init__(self, element=None, next_node=None):
        self.next_node = next_node
        self.element = element

    def __bool__(self):
        return self.element is not None

    def __eq__(self, other):
        return self.element == other

    # We return a pair object in order to have a referrence to the next node.
    def remove(self, element):

        if self == element:
            return self.next_node, True

        if self.next_node is None:
            return self, False

        result = self.next_node.remove(element)
        self.next_node = result[0]
        return self, result[1]


class LinkedList:

    def __init__(self):
        self.root = Node()
        self.size = 0
        self.current = None
        return

    def insert(self, element):
        self.root = Node(element, self.root)
        self.size += 1
        return

    # The only edge check we have to do is the root element,
    # The other 2 cases (in the middle, in the end) can be abstracted and treated as one
    def remove(self, element):
        if self.size == 0:
            return False

        if self.root == element:
            self.root = self.root.next_node
            self.size -= 1
            return True

        current = self.root
        while current.next_node and current.next_node != element:
            current = current.next_node

        res = current.next_node == element
        self.size -= res
        current.next_node = current.next_node if not res else current.next_node.next_node

        return res
    
    # Creates an array with all the elements in O(n), Sorts them in O(nlogn)
    # Overwrites in O(n) -> O(nlogn) runtime.
    def sort(self, comp=None, key=None, reverse=False):
        elements = [x for x in self]
        current = self.root
        for element in sorted(elements, cmp=comp, key=key, reverse=reverse):
            current.element = element

        return self

    # Calls remove element from node object and it recursively removes an element
    # Remove function returns a pair object that contains the new next node
    # (the new root in this case) and a boolean, indicating removal or not of element.
    def remove_recursive(self, element):
        result = self.root.remove(element)
        self.root = result[0]
        removed: bool = result[1]

        if removed:
            self.size -= 1

        return removed

    # toString equivalent
    def __repr__(self):
        return str([x for x in self])

    # Simple iterator function, allows us to write for x in <list>,
    # Equivalent to forEach in Java
    def __iter__(self):
        current = self.root

        while current:
            yield current.element
            current = current.next_node

        return iter(self)

    def __len__(self):
        return self.size


if __name__ == '__main__':
    test_list = LinkedList()

    for x in range(-10, 11):
        test_list.insert(x)
    compare_list = [x for x in range(10, -11, -1)]

    ## TEST 0, all elements are inserted the same

    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)

    ## TEST 1, removing 5 first elements

    for x in range(5):
        assert test_list.remove(10-x) == True
        compare_list.remove(10-x)
    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)

    ## TEST 2, remove 5 elements from the end, -10 up to -6 included.

    for x in range(-6,-11,-1):
        assert test_list.remove(x) == True
        compare_list.remove(x)
    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)

    # TEST 3, remove 2 elements from the start recursively
    # Starting from 5 up to 3.

    for x in range(5,3,-1):
        assert test_list.remove_recursive(x) == True
        compare_list.remove(x)
    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)

    # TEST 4, remove 2 elements from the end recursively
    # Starting from -5 up to -3

    for x in range(-5,-3,1):
        assert test_list.remove_recursive(x) == True
        compare_list.remove(x)
    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)

    # TEST 5, remove 2 elements from the middle
    # Starting from 0 to 1

    for x in range(0,2):
        assert test_list.remove(x) == True
        compare_list.remove(x)
    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)
    # TEST 5, remove 2 elements from the middle recursively with missing elements
    # Starting from 0 to 1

    for x in range(2, -2, -1):
        assert test_list.remove_recursive(x) == (x in compare_list )
        if x in compare_list:
            compare_list.remove(x)

    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)

    # TEST 6, remove 3 elements from middle with some missing

    for x in range(-3, 4, 1):
        assert test_list.remove(x) == (x in compare_list)
        if x in compare_list:
            compare_list.remove(x)
    
    assert [x for x in test_list] == compare_list
    assert len(test_list) == len(compare_list)
    # Test 7, sorting
    from random import randint

    for x in range(20):
        u = randint(-100,100)
        compare_list.append(u)
        test_list.insert(u)
    assert [x for x in sorted(test_list)] == sorted((compare_list))

    print("All tests Passed")
