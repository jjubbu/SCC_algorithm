# 링크드 리스트 문제

# 두 링크드 리스트의 합 계산

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

# 여기서부터 문제 풀기!
def get_linked_list_sum(linked_list_1, linked_list_2):
    
    one = get_linked_list_number(linked_list_1)
    two = get_linked_list_number(linked_list_2)
        
    return one+two

def get_linked_list_number(node):
    result = ""
    cur = node.head
    while cur != None :
        result += str(cur.data)
        cur = cur.next
    return int(result)

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))