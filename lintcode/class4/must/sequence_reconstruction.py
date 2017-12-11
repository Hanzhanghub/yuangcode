# coding:utf-8

'''
date:2017/9/26
content:
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. 
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. 
Reconstruction means building a shortest common supersequence of the sequences in seqs 
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
Example 1:
Input:
org: [1,2,3], seqs: [[1,2],[1,3]]
Output:
false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
Input:
org: [1,2,3], seqs: [[1,2]]
Output:
false
Explanation:
The reconstructed sequence can only be [1,2].

Example 3:
Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
Output:
true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
Output:
true
'''


class Solution(object):
    def sequence_reconstruction(self, org, seqs):
        if not seqs:
            return False

        # step 1
        in_degree, out_degree = self.helper(seqs)

        # step 2: BFS
        queue = []
        results = []

        for i in org:
            if in_degree[i] == 0:
                queue.append(i)
        while len(queue) == 1:
            pop_nom = queue.pop()
            results.append(pop_nom)
            for node in out_degree[pop_nom]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)

        if len(queue) > 1: # 注意这一定得是大于，不能使不等于，否则没有考虑到队列为空的情况
            return False
        return len(results) == len(org) and results == org

    # step 1 helper
    def helper(self, seqs):
        dict_in = {}
        dict_out = {}

        for seq in seqs:
            for i in range(len(seq)):
                if i == 0:
                    dict_in.setdefault(seq[i], 0)
                if i < len(seq) - 1:
                    dict_out.setdefault(seq[i], [])
                    if seq[i + 1] not in dict_out[seq[i]]:
                        dict_out[seq[i]].append(seq[i + 1])
                        dict_in.setdefault(seq[i + 1], 0)
                        dict_in[seq[i + 1]] += 1
                if i == len(seq) -1:
                    dict_out.setdefault(seq[i],[])
        print(dict_in)
        print(dict_out)
        return dict_in, dict_out


if __name__ == '__main__':
    s = Solution()
    org, seqs = [4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]]
    ret = s.sequence_reconstruction(org, seqs)
    print(ret)

'''
1.稍微困难一点的题，就要靠统计入度和出度解决。
2.其实第一步都是统计，只是统计的强度不同。
第二步就是BFS，灵活性在于，入队列的多少，有些题目队列中只能有一个元素（如此题），有些题目队列可以一直入队。

'''