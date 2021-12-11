# 클래스 = 레진틀
# 객체 = 레진으로 커스텀해서 만든 굿즈, 컬러나 들어가는건 다양함

class Human:
    pass # 안에 아무것도 없다는 으미!

human1 = Human()
print(human1)
# <__main__.Human object at 0x10831f340> 
human2 = Human()
print(human2)
# <__main__.Human object at 0x100970520>

# "humal1"이랑 "human2"는 Human으로 만든 "객체" 이고 서로 다름! 
# 그래서 0x뒤에 숫자가 다른것..!




# 클래스의 "생성자"
# 객체를 생성할때 데이터를 넣어주거나 행동을 실행해줌
# 생성자 함수 명칭은 무조건 "__init__" 고정!

# self 는 객체 자신. 객체 = self = {name:Name,age:Age, ...} 같은 느낌.
# 클래스 안에 여러 함수를 넣어서 사용할 수도 있음!

class Person:
    def __init__(self, Name, Age) :
        print("hello",self)
        self.name = Name
        self.age = Age
    def hello(self) :
        print(self.name+"는 안녕이라고 인사합니다.")


person = Person("심선아",26)

print(person.name)
print(person.age)
person.hello()

# 함수랑 비슷하지만 다른점은 클래스를 이용해서 객체 안해 행동과 데이터를 같이 저장할 수 있다는것!
