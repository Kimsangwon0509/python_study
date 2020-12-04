#self의 이해
class SelfTest():
    def func1():
        print('func1 called')
    def func2(self):
        print(id(self))
        print('func2 called')

f = SelfTest()

#print(dir(f))
#print(id(f))
#f.func1()  이것은 에러가 난다. 예외
#f.func2()

#SelfTest.func1() 로 호출해야한다.
#SelfTest.func2() 는 self가 없어서 즉 self로 접근을 안해서 접근이 안된다.
#SelfTest.func2(asd) 등 매개체가 있어야 호출이 된다. 


