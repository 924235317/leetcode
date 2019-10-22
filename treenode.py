class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def list2treenode(l):
    def core(l, idx):
        if idx >= len(l) or not l[idx]:
            return None

        node = TreeNode(l[idx])
        node.left = core(l, 2*idx+1)
        node.right = core(l, 2*idx+2)
        #print(node.val, node.left, node.right)
        
        return node
    return core(l, 0)

def print_treenode(root):
    def print_node(l):
        tmp = list()
        for ll in l:
            if ll:
                tmp.append(ll.val)
            else:
                tmp.append(None)
        print(tmp)

    level = list()
   
    level.append(root)
    while level:
        print_node(level)
        next_level = list()
        flag = False
        for l in level:
            if not l:
                next_level.append(None)
                next_level.append(None)
                continue
            if l.left:
                next_level.append(l.left)
                flag = True
            else:
                next_level.append(None)
                
            if l.right:
                next_level.append(l.right)
                flag = True
            else:
                next_level.append(None)

        if flag:
            level = next_level
        else:
            level = []


def preorder_traversal(root):
    if not root:
        return 

    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def morris_preorder_traversal(root):
    if not root:
        return  

    cur = root
    pre = None

    while cur:
        if cur.left:
            pre = cur.left
            while pre.right and pre.right != cur: 
                pre = pre.right
            if not pre.right:
                print(cur.val)
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                cur = cur.right
        else:
            print(cur.val)
            cur = cur.right

def morris_inorder_traversal(root):
    if not root:
        return

    pre = None
    cur = root

    while cur:
        if not cur.left:
            print(cur.val)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right

            if not pre.right:
                pre.right = cur
                cur = cur.left
            else:
                print(cur.val)
                pre.right = None
                cur = cur.right


if __name__ == "__main__":
    l = [1,2,3,4,None, 6, 7,None,None,None,None,None,None, 14, 15]
    root = list2treenode(l)
    print_treenode(root)
    #preorder_traversal(root)
    morris_preorder_traversal(root)
    morris_inorder_traversal(root)
