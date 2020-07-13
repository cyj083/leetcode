#coding:utf-8
#author:cai yijin <yijin95@163.com>


"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 判断head的长度是不是小于k
    def isLessK(self, head, k):
        i = 0
        cur = head
        while head and i < k:
            head = head.next
            i += 1
        return cur if i < k else head, i < k

    # 反转head的前k位，返回反转后的前k位的head和tail
    def reverseOne(self, head, k):
        tail = head
        prev = None
        for i in range(k):
            nexthead = head.next
            head.next = prev
            prev = head
            head = nexthead
        return prev, tail

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 判断是否小于K
        newHead, isLessK = self.isLessK(head, k)

        # 如果小于K，不反转，直接返回当前节点
        if isLessK:
            return newHead

        # 如果大于等于K，则反转前k位
        head, tail = self.reverseOne(head, k)
        # 递归反转后面的元素
        tail.next = self.reverseKGroup(newHead, k)
        return head

