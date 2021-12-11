# 문제 풀어보기

# 1. 링크드 리스트에서 index번째 원소를 반환하기
# 2. 링크드 리스트의 index번째에 노드 추가하기
# 문제에서 주어진 코드
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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 이 부분부터 수정!
    # index 값에 맞는 노드 가져오기
    def get_node(self, index):
        cur = self.head
        i = 0
        # i랑 index가 맞을때까지 화살표를 이동시켜준다.
        while i != index :
            cur = cur.next
            i+=1
        return cur
    
    # 원소 추가하기
    def add_node(self, index, value):
        new = Node(value)
        # index가 0일때는 노드를 추가하려는 위치에 이전 노드가 없다.
        # 따라서 추가하고자 하는 노드는 맨 앞에 넣어져 이 링크드 리스트의 머리(head)가 된다.
        if index == 0 :
            new.next = self.head
            self.head = new
            return
        # index가 0이 아니라면 지금 위치의 next 노드를 저장하고
        # 추가하려는 노드를 앞에것에 붙인 뒤 저장해둔 다음 노드를 붙여준다. 
        # 노드들은 전부 "next" 로 연결되어있고 이 정보는 저장되어있어서
        # 중간의 next를 끊고 새 것을 추가하고 다시 연결해도
        # 그 다음의 노드들의 연결은 끊겨있지않는다.
        
        # 여기서 here은 원소를 추가할 위치에 원래 있던 노드
        here = self.get_node(index-1)
        prev = here.next 
        here.next = new
        new.next = prev
    
    def delete_node(self, index):
        if index == 0 :
            self.head = self.head.next
            return
        after = self.get_node(index).next
        before = self.get_node(index-1)
        before.next = after
        return "index 번째 Node를 제거해주세요!"

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.append(8)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.add_node(1, 3)
linked_list.print_all()
linked_list.delete_node(2)
linked_list.print_all()

