class Solution(object):
    def inorder(self, root):
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans
    def rangeSumBST(self, root, low, high):
        c=0
        x=self.inorder(root)
        for y in x:
            if low<=y<=high:
                c+=y
        return c
        def rangeSumBST(self, root, low, high):
            c=0
            x=self.inorder(root)
            for y in x:
                if low<=y<=high:
                    c+=y
            return c