import Queue
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        out_str = ''
        value_store = Queue.Queue()
        if root is None:
            return None
        else:
            value_store.put(root)

        while not value_store.empty():
            node = value_store.get()
            if node is None:
                out_str += 'null' + ' '
            else:
                out_str += str(node.val) + ' '
                if node.left is not None:
                    value_store.put(node.left)
                else:
                    value_store.put(None)
                if node.right is not None:
                    value_store.put(node.right)
                else:
                    value_store.put(None)

        return out_str

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
    codec = Codec()
    data = '1'
    deserialize_out = codec.deserialize(data)
    serialize_out = codec.serialize(deserialize_out)
    print serialize_out

if __name__ == '__main__':
    main()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))