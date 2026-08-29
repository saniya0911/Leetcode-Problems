# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
    #     data = self.preorder_serialise(root)
    #     return data
    # def preorder_serialise(self, root):
    #     if not root:
    #         return '*'
    #     return ','.join([str(root.val), self.preorder_serialise(root.left), self.preorder_serialise(root.right)])
        data = ""
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                data += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
            else:
                data += '*' + ','

        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
    #     nodes = deque()
    #     nodes.extend(data.split(','))
    #     root = self.preorder(nodes)
    #     return root

    # def preorder(self, nodes):
    #     root = nodes.popleft()
    #     if root == '*':
    #         return None
    #     node = TreeNode(int(root))
    #     node.left = self.preorder(nodes)
    #     node.right = self.preorder(nodes)
    #     return node
        print(data)
        nodes = data.split(',')
        if nodes[0] == '*':
            return None
        q = deque()
        root = TreeNode(int(nodes[0]))
        q.append(root)
        i = 1
        while q:
            node = q.popleft()
            if i < len(nodes) and nodes[i] != '*':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i +=1
            if i < len(nodes) and nodes[i] != '*':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i +=1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))