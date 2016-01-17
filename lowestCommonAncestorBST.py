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

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p is None or q is None:
            return None
        node = root
        while True:
            if p is node.val or q is node.val:
                return node
            if p < node.val < q or q < node.val < p:
                return node
            if p < node.val and q < node.val:
                node = node.left
            if p > node.val and q > node.val:
                node = node.right
        return None


def main():
    sol = Solution()
    #data = '6 2 8 0 4 7 9 null null 3 5 null null null null'
    data = '2 1 null null null'
    deserialize_out = sol.deserialize(data)
    p = 2
    q = 1
    out = sol.lowestCommonAncestor(deserialize_out, p, q)
    print(out.val)

if __name__ == '__main__':
    main()