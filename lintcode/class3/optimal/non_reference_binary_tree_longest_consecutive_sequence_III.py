# coding:utf-8
'''
Description
It's follow up problem for Binary Tree Longest Consecutive Sequence II

Given a k-ary tree, find the length of the longest consecutive sequence path.
The path could be start and end at any node in the tree

Example
An example of test data: k-ary tree 5<6<7<>,5<>,8<>>,4<3<>,5<>,3<>>>, denote the following structure:


     5
   /   \
  6     4
 /|\   /|\
7 5 8 3 5 3

Return 5, // 3-4-5-6-7
'''

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def longest_consecutive_path(self,root):
