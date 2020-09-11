class Node:
    
    def __init__(self, value: int, name: str, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
        self.name = name


def buildExampleTree():
    node1 = Node(1,'node1')
    node2 = Node(1,'node2')
    node3 = Node(1, 'node3', node1, node2)
    node4 = Node(0,'node4')
    node5 = Node(1,'node5')
    node6 = Node(0,'node6', node3, node4)
    node7 = Node(0, 'node7', node5, node6)
    
def trCountUnival(root):
    count = 0 
    countUnival(root,count)
    return count

def countUnival(node: Node, count):
    if node.left is not None:
        countUnival(node.left,count)
    if node.right is not None:
        countUnival(node.right,count)
    if areDescendentsEqual(node):
        print(f"{node.name}: {count}")

def numberUnivalAtOrBelow(node):
    number = 0 
    if node.left is not None:
        number += numberUnivalAtOrBelow(node.left)
    if node.right is not None:
        number += numberUnivalAtOrBelow(node.right)
    if areDescendentsEqual(node):
        number += 1
    return number

#def areChildrenEqual(node: Node):
#    
#    if node.left is None and node.right is None:
#        return True
#    elif node.left is None:
#        return False
#    elif node.right is None:
#        return False
#    if node.left.val == node.right.val:
#        return True
#    return False
#

def areDescendentsEqual(node):
    if node.left is None: 
        left = True
    else: 
        left = areDescendentsEqual(node.left)
        
    if node.right is None: 
        right = True
    else: 
        right = areDescendentsEqual(node.right)

    if node.left is not None and node.right is not None and node.left.val != node.right.val:
        equal = False
    else:
        equal = True
    return left and right and equal

    


