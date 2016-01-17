import Queue
#Definition for a  binary tree node


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


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.store_val = []
        self.has_next = False
        self.current_idx = -1
        self.len_store = 0
        self.stack_store = []
        self.in_order_traverse(root)

    def call_traverse(self, node):
        while True:
            if node is not None:
                self.stack_store.append(node)
                node = node.left
            else:
                if len(self.stack_store) > 0:
                    node = self.stack_store.pop()
                    self.store_val.append(node.val)
                    node = node.right
                else:
                    break
        self.len_store = len(self.store_val)

    def in_order_traverse(self, root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            self.store_val.append(root.val)
            self.len_store = 1
            return True

        node = root.left
        if node is None:
            node = root.right
            self.store_val.append(root.val)

        self.call_traverse(node)

        if root.left is not None:
            self.stack_store.append(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        self.current_idx += 1
        if self.current_idx < self.len_store:
            return True
        elif len(self.stack_store) > 0:
            node = self.stack_store.pop()
            self.store_val.append(node.val)
            node = node.right
            self.call_traverse(node)
            return True
        else:
            return False

    def next_v(self):
        """
        :rtype: int
        """
        val = self.store_val[self.current_idx]
        return val


def main():
    data = '8 3 10 1 6 null 14 null null 4 7 13 null'
    sol = Solution()
    deserialize_out = sol.deserialize(data)
    # Your BSTIterator will be called like this:

    i, v = BSTIterator(deserialize_out), []
    while i.hasNext():
        v.append(i.next_v())
    print(v)


if __name__ == '__main__':
    main()
