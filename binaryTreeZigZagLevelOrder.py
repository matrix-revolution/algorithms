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

    def bfs(self, node):
        output = []
        store = []
        store.append(node)
        store.append(None)
        output.append(node.val)
        output.append(None)
        k = 0
        while len(store) > k:
            val = store[k]
            if val is not None:
                node = val.left
                if node is not None:
                    store.append(node)
                    output.append(node.val)
                node = val.right
                if node is not None:
                    store.append(node)
                    output.append(node.val)
            else:
                if len(store)-1 != k:
                    store.append(None)
                    output.append(None)
            k += 1
        return output

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        val_store = []
        inner_list = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            inner_list.append(root.val)
            output.append(inner_list)
            return output
        val_store = self.bfs(root)
        k = 0
        flag = 1
        while k < len(val_store):
            if flag:
                inner_list = []
                while val_store[k] is not None:
                    inner_list.append(val_store[k])
                    k += 1
                if val_store[k] is None:
                    output.append(inner_list)
                    k += 1
                    flag = not flag
            else:
                inner_list = []
                m = k
                n = k
                while val_store[n] is not None:
                    n += 1
                if val_store[n] is None:
                    k = n
                    n -= 1
                while n >= m:
                    inner_list.append(val_store[n])
                    n -= 1
                output.append(inner_list)
                k += 1
                flag = not flag
        return output


def main():
    sol = Solution()
    data = '3 9 20 null null 15 7'
    deserialized_out = sol.deserialize(data)
    output = sol.zigzagLevelOrder(deserialized_out)
    print(output)

if __name__ == '__main__':
    main()