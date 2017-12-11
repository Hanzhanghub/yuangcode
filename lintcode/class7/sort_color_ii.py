# coding:utf-8


'''
date: 2017/11/15
content: 
Given an array of n objects with k different colors (numbered from 1 to k), 
sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Notice
You are not suppose to use the library's sort function for this problem.
k <= n

Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
'''


class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # special
        if not colors or k == 1:
            return

        # solution 1: quick sort
        self.quickSort(colors, 0, len(colors) - 1)

        # solution 2: rainbow sort ps: Actually, I think it's a variation of the quick sort
        self.rainbowSort(colors, 0, len(colors) - 1, 1, k)

        return colors

    def quickSort(self,
                  colors,
                  start,
                  end):
        if start >= end:
            return

        left = start
        right = end
        pivot = colors[(start + end) // 2]

        while left <= right:
            while left <= right and colors[left] < pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1

            if left <= right:
                tmp = colors[left]
                colors[left] = colors[right]
                colors[right] = tmp
                left += 1
                right -= 1

        self.quickSort(colors, start, right)
        self.quickSort(colors, left, end)

    def rainbowSort(self,
                    colors,
                    start,
                    end,
                    colorFrom,
                    colorTo):
        if colorFrom == colorTo:
            return

        if start >= end:
            return

        left = start
        right = end
        colorMid = (colorFrom + colorTo) // 2

        while left <= right:
            while left <= right and colors[left] < colorMid:
                left += 1
            while left <= right and colors[right] > colorMid:
                right -= 1

            if left <= right:
                tmp = colors[left]
                colors[left] = colors[right]
                colors[right] = tmp

                left += 1
                right -= 1
        self.rainbowSort(colors, start, right, colorFrom, colorMid)
        self.rainbowSort(colors, left, end, colorMid + 1, colorTo)


if __name__ =='__main__':
    a = [3, 2, 2, 1, 4]
    s = Solution()
    ret = s.sortColors2(a, 4)
    print(ret)


'''
解法1： 直接使用快速排序，时间复杂度为 nlog(n).
解法2： 使用快速排序的变种彩虹排序（rainbow sort）,时间复杂度为 nlog(k):
    (1) 在快速排序的递归调用上增加两个参数colorFrom和colorTo，分别表示着小于k/2和大于k/2+1的颜色
    (2) 当colorFrom和colorTo相等时，就说明某一部分已经完成了排序。
    (3) 其余过程和快速排序一样
'''

