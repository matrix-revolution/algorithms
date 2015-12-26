import Queue
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        count = 1
        node_queue = Queue.Queue()
        node_queue.put(root)
        node_queue.put('null')
        while not node_queue.empty():
            node = node_queue.get()
            if node == 'null':
                if not node_queue.empty():
                    count += 1
                    node_queue.put('null')
            elif node is not None:
                if node.left is not None or node.right is not None:
                    node_queue.put(node.left)
                    node_queue.put(node.right)
        return count

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


def main():
    sol = Solution()
    data = '1 2 5 3 null 7 9 null null 8 10 null null null null 13 null'
    deserialize_out = sol.deserialize(data)
    depth = sol.max_depth(deserialize_out)
    print depth

if __name__ == '__main__':
    main()