# coding:utf-8

'''
date:2017/9/21
content:
设计一个算法，并编写代码来序列化和反序列化二叉树。
将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，
你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。

There is no limit of how you deserialize or serialize a binary tree, 
LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.
样例
给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如下的树结构：
  3
 / \
9  20
  /  \
 15   7
我们的数据是进行BFS遍历得到的。当你测试结果wrong answer时，你可以作为输入调试你的代码。

你可以采用其他的方法进行序列化和反序列化。
'''

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # BFS
        serialize_string = []
        default_flag = "#"
        queue = []

        if root is None:
            return serialize_string

        queue.append(root)
        while queue:
            queue_size = len(queue)
            tmp = []
            for i in range(queue_size):
                node = queue.pop(0)

                if node == default_flag:
                    tmp.append(default_flag)
                    continue
                else:
                    tmp.append(str(node.val))

                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(default_flag)

                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(default_flag)
            serialize_string += tmp

        serialize_string = ','.join(serialize_string)
        serialize_string = '{' + serialize_string + '}'

        return serialize_string


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # pass
        default_flag = "#"
        deserialize_root = None
        if not data:
            return deserialize_root

        data = data[1:-1].split(',')
        data_init_pop = data.pop(0)
        deserialize_root = TreeNode(int(data_init_pop))
        queue = []
        queue.append(deserialize_root)

        while queue:
            tmp = []
            queue_size = len(queue)

            for i in range(queue_size):
                data_0 = data.pop(0)
                data_1 = data.pop(0)
                node = queue.pop(0)
                if data_0 != default_flag:
                    node.left = TreeNode(int(data_0))
                    queue.append(node.left)
                if data_1 != default_flag:
                    node.right = TreeNode(int(data_1))
                    queue.append(node.right)

        return deserialize_root



if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    s = Solution()
    ret_1 = s.serialize(tree)
    # print(ret)
    # a = ret[1:-1].split(',')
    # print(a)
    ret_2 = s.deserialize(ret_1)
    ret_3 = s.serialize(ret_2)
    print(ret_3)

'''
1.序列化及反序列化均可用BFS层级遍历实现
2.反序列化可以用两个队列的出入栈理解
'''


