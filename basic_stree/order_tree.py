# copy: https://blog.yangx.site/2016/07/22/Python-binary-tree-traverse/
class BinNode:
    def __init__(self, data, leftNode=None, rightNode=None):
        self.data = data
        self.left = leftNode
        self.right = rightNode


def pre_order(rootNode):
    """实现先序遍历

    先序遍历是先访问根节点，然后访问左子树，最后访问又子树

    Args:
      rootNode: 树的根节点
    """
    if rootNode == None:
        return
    print(rootNode.data)
    pre_order(rootNode.left)
    pre_order(rootNode.right)

#中序遍历
def in_order(rootNode):

    if rootNode is None:
        return
    in_order(rootNode.left)
    print(rootNode.data)
    in_order(rootNode.right)

#后序遍历
def post_order(rootNode):
    if rootNode is None:
        return
    post_order(rootNode.left)
    post_order(rootNode.right)
    print(rootNode.data)

#不使用递归的方法来先序遍历
def pre_order_no_rec(rootNode):

    stack = []
    node = rootNode

    while node or stack:
        while node is not None:
            print(node.data)
            stack.append(node.right)
            node = node.left
        node = stack.pop()

#不使用递归的方法来进行中序遍历
def in_order_no_rec(rootNode):
    stack = []
    node = rootNode

    while node or stack:
        print('stack len is %d' % len(stack))
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.data)
        node = node.right

#不使用递归的后序遍历
def post_order_no_rec(rootNode):
    stack = []
    node = rootNode

    while node or stack:
        while node:
            stack.append(node)
            node = node.left if node.left else node.right   # 找到左下角的元素

        node = stack.pop()
        print(node.data)

        if stack and stack[-1].left == node:
            node = stack[-1].right
        else:
            node = None

#用两个栈来实现后序遍历
def post_order_two_stack(rootNode):
    stack1 = []
    stack2 = []
    node = rootNode

    stack1.append(node)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        print(stack2.pop().data)
        
#层次遍历
def level_order(rootNode):
    queue = []
    node = rootNode
    queue.append(node)

    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == '__main__':

    four = BinNode(4)
    five = BinNode(5)
    six = BinNode(6)
    seven = BinNode(7)

    two = BinNode(2, four, five)
    three = BinNode(3, six, seven)
    one = BinNode(1, two, three)

    post_order_no_rec(one)
    post_order(one)
