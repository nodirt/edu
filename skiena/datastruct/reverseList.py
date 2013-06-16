class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def toNodes(items):
    first = None
    last = None
    for x in items:
        node = Node(x)
        if first is None:
            first = node
        else:
            last.next = node
        last = node
    return first


def toList(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result


def reverse(node):
    first = None

    def rev(node):
        if node is None:
            return node
        result = Node(node.value)
        nonlocal first
        prev = rev(node.next)
        if first is None:
            first = result
        if prev is not None:
            prev.next = result
        return result

    rev(node)
        
    return first


def test(items):
    expected = list(reversed(items))
    actual = toList(reverse(toNodes(items)))
    assert(expected == actual)


test([1, 2, 3])
test([])
test([1])