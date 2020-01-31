total = 0

def pathSum(root, sum):
    def dfs(root, sum):
        if not root:
            return 0

        if root.val == sum:
            total += 1

        dfs(root.left, sum - root.val)
        dfs(root.right, sum - root.val)

    def pathSumCore(root, sum):
        if not root:
            return 0

        dfs(root, sum)
        pathSum(root.left, sum)
        pathSum(root.right, sum)
    
    pathSumCore(root, sum)
    return total

