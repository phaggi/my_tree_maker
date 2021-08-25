import random
import string
from pprint import pprint


class Node:
    def __init__(self, name: str, parent: 'Node' = None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, obj: 'Node'):
        self.children.append(obj)


class Tree:
    def __init__(self, tree_source: list):
        self.tree_source = tree_source
        self.prepare_tree_source()
        self.tree_by_node = dict()
        self.tree_by_node[None] = Node('ROOT', None)
        self.make_tree_by_node()
        self.tree_recursive = {None: {}}
        self.make_tree_recursive()
        self.tab = " "

    def change_node_none(self, from_value, to_value):
        for number, items in enumerate(self.tree_source):
            if items[0] is from_value:
                self.tree_source[number] = (to_value, items[1])

    def prepare_tree_source(self):
        to_value = '_____' + ''.join([random.choice(string.ascii_lowercase) for i in range(10)])
        self.change_node_none(None, to_value)
        self.tree_source = sorted(self.tree_source)
        self.change_node_none(to_value, None)

    def make_tree_by_node(self):
        for parent, child in self.tree_source:
            parent_node = self.tree_by_node[parent]
            if child not in self.tree_by_node:
                self.tree_by_node[child] = Node(child, parent_node)
            parent_node.add_child(self.tree_by_node[child])

    def print_tree(self, node=None, level=0):
        root = self.tree_by_node[node]
        if root.children:
            level += 1
            for child in root.children:
                self.print_line(child.name, level)
                self.print_tree(child.name, level)
            level -= 1

    def pprint_recursive_tree(self):
        pprint(self.tree_recursive)

    def print_line(self, name, level):
        print(f'{self.tab * level}{name}')

    def add_child_to_tree_by_node(self, child: 'Node'):
        pass

    def add_child_to_tree_recursive(self, child: 'Node'):
        pass

    def make_tree_source(self):
        pass

    def add_node_to_tree_recursive(self, node: tuple, tree: dict):
        in_parent, in_child = node
        if in_parent in tree:
            if isinstance(tree[in_parent], dict):
                tree[in_parent].update({in_child: {}})
        else:
            for key in tree:
                self.add_node_to_tree_recursive(node, tree[key])
        return tree

    def make_tree_recursive(self):
        for parent, child in self.tree_source:
            self.add_node_to_tree_recursive((parent, child), self.tree_recursive)


if __name__ == '__main__':
    input_tree = [
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
        (None, 'a')
    ]

    my_tree = Tree(input_tree)
    my_tree.print_tree()
    my_tree.pprint_recursive_tree()
