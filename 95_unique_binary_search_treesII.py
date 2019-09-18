from treenode import *

def generateTrees(n: int) -> list:
    def generateTreesCore(l: int, r: int) -> list:
        res = list()

        if l > r:
            return None 

        if l == r:
            return [TreeNode(l)]

        for i in range(l, r+1):
            
            l_nodes = generateTreesCore(l, i-1)
            r_nodes = generateTreesCore(i+1, r)

            for ll in l_nodes:
                for rr in r_nodes:
                    cur_node = TreeNode(i)
                    cur_node.left = ll
                    cur_node.right = rr
                    res.append(cur_node)

        return res
    
    return generateTreesCore(1, n)
