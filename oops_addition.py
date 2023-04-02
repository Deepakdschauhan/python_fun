class calcu:
    def add(self,a,b):
        self.a=a
        self.b=b

        print(a+b)
    def mult(self,a,b):
        self.a=a
        self.b=b
        print(a*b)
    
obj1=calcu()
print(obj1.add(5, 6))
print(obj1.mult(5, 5))