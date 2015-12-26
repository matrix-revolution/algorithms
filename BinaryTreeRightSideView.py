__author__ = 'rajeevkumar'

import collections;
# Definition for a binary tree node.


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        output = []
        bfsQueue = collections.deque([root, None]);
        rightNodeAtlevelFound = false;
        while(len(bfsQueue)):
            rightNode = bfsQueue.popleft();
            if(rightNode == None):
                if (len(bfsQueue)):
                    bfsQueue.append(None);
            elif rightNodeAtlevelFound == false:
                output.append(rightNode.val);
                if (rightNode.right != None):
                    bfsQueue.append(rightNode.right)
                if (rightNode.left != None):
                    bfsQueue.append(rightNode.left)
            else
                if (rightNode.right != None):
                    bfsQueue.append(rightNode.right)
                if (rightNode.left != None):
                    bfsQueue.append(rightNode.left)


