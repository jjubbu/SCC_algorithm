# 큐
# 빨대같은 구조.. 한쪽에서 넣고 들어온 순서대로 반대쪽에서 빼는 구조.
# FIFO(First in First Out)

# 큐의 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        return

    def dequeue(self):
        # 어떻게 하면 될까요?
        return

    def peek(self):
        # 어떻게 하면 될까요?
        return

    def is_empty(self):
        # 어떻게 하면 될까요?
        return