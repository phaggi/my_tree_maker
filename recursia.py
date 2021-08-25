from pprint import pprint

def add_node_to_recursive_tree(node: tuple, tree: dict):
    in_parent, in_child = node
    if in_parent in tree:
        if isinstance(tree[in_parent], dict):
            tree[in_parent].update({in_child: {}})
    else:
        for key in tree:
            add_node_to_recursive_tree(node, tree[key])
    return tree


def make_recursive_tree(in_tree: list):
    result_tree = {None: {}}
    for parent, child in in_tree:
        add_node_to_recursive_tree((parent, child), result_tree)
    return result_tree


if __name__ == '__main__':
    input_tree = [
        (None, 'a'),
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
    ]
    pprint(make_recursive_tree(input_tree))
