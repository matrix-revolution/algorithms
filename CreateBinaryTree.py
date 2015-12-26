__author__ = 'rajeevkumar'
import Tree;
import collections;

def CreateBinaryTreeFromList(numbers):
    if len(numbers) == 0:
        return None;
    tree = Tree.TreeNode;
    tree.val = numbers[0];
    levelNodeQueue = collections.deque;
    leftTurn = true;
    for number in numbers[1:]:


