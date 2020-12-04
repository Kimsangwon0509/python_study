# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    #클래스 변수
    stock_num = 0 #재고

    def __init__(self,name):
        #인스턴스 변수 내것 나만의것
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):
        Warehouse.stock_num -= 1

user1 =Warehouse('Lee')
user2 =Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print(user1.stock_num)

del user1
print(Warehouse.__dict__)