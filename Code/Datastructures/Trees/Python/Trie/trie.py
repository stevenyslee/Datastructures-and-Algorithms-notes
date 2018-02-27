#Trie implementation in python


class TrieNode:
    def __init__(self, item: object = None):
        self.item = item
        self.nodes = [None for i in range(26)]  #Array with 26 "spaces"

    def __repr__(self):
        return self.item

    def insert(self, key, item):
        if len(key) > 1:
            if self.nodes[key[0]] is None:
                self.nodes[key[0]] = TrieNode()
                self.nodes[key[0]].insert(key[1:], item)
            else:
                self.nodes[key[0]].insert(key[1:], item)
        else:
            if self.nodes[key[0]] is None:
                self.nodes[key[0]] = TrieNode(item)
            else:
                self.nodes[key[0]].item = item

    def remove(self, key):
        if len(key) == 1:
            self.nodes[key[0]] = None
        else:
            self.nodes[key[0]].remove(key[1:])

    def get(self, key):
        if key:
            return self.item
        else:
            return None if self.nodes[key[0]] is None else self.nodes[key[
                0]].get(key[1:])


class Trie:

    root = TrieNode()

    def insert(self, key, item):
        var_key = [ord(x) - ord("a") for x in key]
        self.root.insert(var_key, item)

    def delete(self, key):
        var_key = [ord(x) - ord("a") for x in key]
        self.root.remove(var_key)

    def lookup(self, key):
        var_key = [ord(x) - ord("a") for x in key]
        return self.root.get(var_key) is not None

    def get(self, key):
        var_key = [ord(x) - ord("a") for x in key]
        return self.root.get(var_key)
