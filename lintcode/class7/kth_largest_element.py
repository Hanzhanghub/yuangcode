# coding:utf-8

'''
date: 2017/11/13
content:
在数组中找到第k大的元素

注意事项
可以交换数组中的元素的位置

样例
给出数组 [9,3,2,4,8]，第三大的元素是 4
给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推
'''


class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        # special condition
        if not A:
            return

        # quick select
        target = self.quick_select(A, 0, len(A) - 1, k)

        return target

    def quick_select(self, a, start, end, k):
        if start == end:
            return a[start]  # watch out for this

        pivot = a[(start + end) // 2]
        left = start
        right = end

        while left <= right:
            while left <= right and a[left] > pivot:
                left += 1

            while left <= right and a[right] < pivot:
                right -= 1

            if left <= right:
                tmp = a[right]
                a[right] = a[left]
                a[left] = tmp
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quick_select(a, start, right, k)

        if start + k - 1 >= left:
            return self.quick_select(a, left, end, k - (left - start))

        return a[right + 1]


if __name__ == '__main__':
    a = [9,3,2,4,8]
    s = Solution()
    ret = s.kthLargestElement(3,a)
    print(ret)

'''
1. quick select和quick sorted在排序上的思路是一样的，基本的写法也一样。除了quick select在最后要考虑到
kth的数在左侧还是右侧
2. 在这道求解第k个最大的问题，我们将partition按照从大到小的顺序进行快排。
3. 在选择k是在左侧还是右侧时，考虑：
        start ..(1).. right .(3). left ..(2)..end 
        （1）如果从头（start）开始，第k个数的位置在right内，则从start到right进行下次快排
        （2）如果从头（start）开始，第k个数的位置超过了right，在left到尾（end）了，则从left到end进行下次快排，
             并且这回要找的是第k-(left-start)个最大了
        （3）如果不是上面两种情况，则为right和left中间的那个数
'''