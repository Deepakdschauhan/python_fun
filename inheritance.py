class parent:
    def func1(self):
        print("first statement of parent class")
    
class child(parent):
    def func2(self):
        print("this is child class statement")

obj1=child()
obj1.func1()
obj1.func2()