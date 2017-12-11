# coding:utf-8

'''
date:2017/11/20
content:
用两个队列实现一个栈，实现push(element)，pop()，top()和isEmpty()方法
'''
class MyStack(object):
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        tmp_queue = []
        ret = None
        for i in range(len(self.queue)):
            if i == len(self.queue) -1:
                ret = self.queue.pop(0)
            else:
                tmp_queue.append(self.queue.pop(0))
        self.queue = tmp_queue

        return ret

    def top(self):
        ret = self.queue.pop(0)
        self.queue.append(ret)
        return ret

    def isEmpty(self):
        return len(self.queue) == 0


'''
1.使用queue的pop操作完成stack的pop操作
    （1）self.queue每次弹出他的开头元素，pop(0)，push到tmp_queue中。直到self.queue中只剩下一个元素（即为stack
         要pop出的元素），将这最后一个元素返回
    （2）将tmp_queue中的元素通过pop(0)重新push进self.queue中
'''

