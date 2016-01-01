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

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        out = []
        while root is not None:
            while root.left is not None:
                stack.append(root)
                root = root.left
            out.append(root.val)
            while root.right is None:
                if len(stack) > 0:
                    root = stack.pop()
                    out.append(root.val)
                else:
                    return out
            root = root.right
        return out


def main():
    sol = Solution()
    data = '1 2 3 4 5 6 7 null null 8 null null null null 9'
    deserialize_out = sol.deserialize(data)
    output = sol.inorderTraversal(deserialize_out)
    print(output)

if __name__ == '__main__':
    main()
