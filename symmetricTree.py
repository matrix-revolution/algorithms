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

    def check_recursively(self, left_tree, right_tree):
        left_side = False
        right_side = False
        if left_tree is None and right_tree is None:
            return True
        if left_tree is None:
            return False
        if right_tree is None:
            return False

        if left_tree.val == right_tree.val:
            left_side = self.check_recursively(left_tree.left, right_tree.right)
            right_side = self.check_recursively(left_tree.right, right_tree.left)
        if left_side and right_side:
            return True
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_tree = root.left
        right_tree = root.right
        if left_tree is None and right_tree is None:
            return True
        elif left_tree is None:
            return False
        elif right_tree is None:
            return False

        if left_tree.val != right_tree.val:
            return False
        else:
            left_side = True
            right_side = True

        left_side = self.check_recursively(left_tree.left, right_tree.right)

        right_side = self.check_recursively(left_tree.right, right_tree.left)

        if left_side and right_side:
            return True
        else:
            return False


def main():
    sol = Solution()
    data = '1 2 2 3 4 3 3'
    deserialize_out = sol.deserialize(data)
    out = sol.isSymmetric(deserialize_out)
    print(out)

if __name__ == '__main__':
    main()
