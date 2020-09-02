class Node:
    
    def __init__(value: int, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def buildExampleTree():
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(1, node1, node2)
    node4 = Node(0)
    node5 = Node(1)
    node6 = Node(0, node3, node4)
    node7 = Node(0, node5, node6)
    
def countUnival(root: Node):
    toCheck = [root]
    for i in range(len(toCheck)):
        newToCheck = []
       # if toCheck[i].left != toCheck[i].right:
       #     if toCheck[i].left is not None: 
       #         newToCheck.append(toCheck[i].left)

       #     if toCheck[i].right is not None: 
       #         newToCheck.append(toCheck[i].right)
        
def areChildrenEqual(node: Node):
    
    if node.left is None and node.right is None:
        return True
    elif node.left is None:
        return False
    elif node.right is None:
        return False
    if node.left.val == node.right.val:
        return True
    return False


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

    


