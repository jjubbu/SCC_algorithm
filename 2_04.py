# 링크드 리스트 만들어보기


# 1. 노드 클래스 생성

class N:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# self.next 는 이 노드의 다음으로 연결할 노드를 말한다.
# None 으로 설정해놓으면 옆에 아무것도 없다는 뜻!

n1 = N(3) # "n1"이라는 노드에 3이 저장됨.
print("n1의 데이터는? " , n1.data) # => 3
n2 = N(5) # "n2"이라는 노드에 5가 저장됨.
print("n2의 데이터는? " , n2.data) # => 5

# 2. 노드들 연결하기

n1.next = n2 # 이러면 [n1] -> [n2] 가 된다!
print("n1의 다음 노드의 데이터는? " , n1.next.data) # n1의 다음 노드의 데이터 = n2의 데이터 = 5 출력

# 위와 같은 코드를 반복해야 링크드 리스트를 만들 수 있으나 하나하나 하기 번거롭다.
# 좀 더 편하게 하려면 클래스 만들기!

# 링크드 리스트 만드는 클래스 만들어보기

class Linked:
    # 링크드 리스트에 넣을 노드를 처음 생성할때 head에 넣는다.
    def __init__(self,val):
        self.head = N(val)
    
    # 새로운 노드를 맨 뒤에 연결하는 행동
    def link_node(self, val):
        # cur은 링크드 리스트의 맨 앞 노드
        cur = self.head
        
        # 마지막 노드의 다음은 None, 따라서 cur의 위치를 맨 뒤로 이동시킨다.
        # cur은 콘솔 게임에서 좌우로만 움직여 아이탬을 가리켜주는 화살표같은것.
        while cur.next != None :
            cur = cur.next
        # cur 이라는 화살표는 현재 맨 뒤의 노드를 가리켜주고있다.
        # 화살표가 가리키는 노드의 다음으로 새로운 노드를 붙여준다.
        cur.next = N(val)
    
    def all_node(self):
        result = []
        cur = self.head
        # cur 화살표를 계속 이동하다보면 아무것도 없는 None 을 가리키게된다.
        # 이때 while 문을 멈추고 모든 노드의 데이터가 들어간 리스트를 출력해준다.
        while cur != None:
            result.append(cur.data)
            cur = cur.next
        print("모든 노드의 배열?" , result)
        
        
link = Linked(5)
link.link_node(3)
link.link_node(7)
# [5]->[3]->[7]
print("link의 head의 데이터는? " , link.head.data)

link.all_node() # => 모든 노드의 배열? [5, 3, 7]