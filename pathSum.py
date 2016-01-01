import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node = TreeNode(0)
        root = node
        data_array = data.split(' ')
        is_root = False
        bin_constraint = 0
        node_queue = Queue.Queue()

        len_data = len(data_array)
        count = 0

        while count < len_data:
            element = data_array[count]
            if not is_root:
                if element is None:
                    return None
                else:
                    is_root = True
                    node.val = int(element)
                    node_queue.put(node)
                    count += 1
            else:
                node = node_queue.get()
                if bin_constraint == 0:
                    if element != 'null':
                        node.left = TreeNode(int(element))
                        node_queue.put(node.left)
                    bin_constraint += 1
                count += 1

                if bin_constraint == 1:
                    element = data_array[count]
                    if element != 'null':
                        node.right = TreeNode(int(element))
                        node_queue.put(node.right)
                    bin_constraint = 0
                count += 1

        return root

    def is_leaf(self, node):
        if node.left is not None or node.right is not None:
            return False
        else:
            return True

    def call_dfs(self, node, root, sum, val):
        if node is None:
            return val
        val += node.val
        if val == sum and self.is_leaf(node):
            return val
        elif abs(val) > abs(sum):
            return val - node.val

        val = self.call_dfs(node.left, root, sum, val)
        if val == sum and self.is_leaf(node):
            return val
        else:
            if node == root:
                val = node.val
            val = self.call_dfs(node.right, root, sum, val)
            if val == sum and self.is_leaf(node):
                return val
        return val

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        head = root
        if sum == 0:
            return False
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        elif root.val == sum:
            return False
        val = self.call_dfs(root, head, sum, 0)
        if val == sum:
            return True
        else:
            return False


def main():
    sol = Solution()
    sum_v = 3
    data = '1 2 null'
    deserialize_out = sol.deserialize(data)
    output = sol.hasPathSum(deserialize_out, sum_v)
    print output

if __name__ == '__main__':
    main()