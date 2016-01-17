# Definition for a binary tree node.
import Queue
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

    def call_recur(self, node, p, q):
        dummy_node = TreeNode(-1)
        if node is None:
            return dummy_node
        curr_node = None
        if p == node.val or q == node.val:
            curr_node = node

        out_left = self.call_recur(node.left, p, q)
        out_right = self.call_recur(node.right, p, q)

        if out_left.val != -1 and out_right.val != -1:
            return node
        if out_left.val != -1:
            if curr_node is not None:
                return curr_node
            return out_left
        if out_right.val != -1:
            if curr_node is not None:
                return curr_node
            return out_right
        if curr_node is not None:
            return curr_node
        return dummy_node

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        out = self.call_recur(node, p, q)
        return out


def main():
    sol = Solution()
    #data = '3 5 1 6 2 0 8 null null 7 4 null null null null null null null null'
    data = '1 2 null null null'
    deserialize_out = sol.deserialize(data)
    p = 1
    q = 2
    out = sol.lowestCommonAncestor(deserialize_out, p, q)
    if out is None:
        print('None')
    else:
        print(out.val)

if __name__ == '__main__':
    main()