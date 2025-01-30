# learn advance OOP

class A:
      classVar = 0
      def __init__(self):
            print("Constructor of A")
            self.Name = "A"
            self.Age = 21
      
      def method(self):
            print("Method 1 of A")
      
      # staticmethod
      @staticmethod
      def staticMethod():
            print("Static Method 2 of A")
      
      @classmethod
      def classMethod(cls):
            print("Class Method 3 of A")
            print(cls)
      
      @property
      def name(self):
            return self.Name
      
      @name.setter
      def name(self,value):
            if value=="A":
                  print("Name can't be A")
                  return
            self.Name=value
      
      @name.deleter
      def name(self):
            del self.Name
      
      
a=A()
a.method()
A.staticMethod()
A.classMethod()
print(a.name)
a.name="A"
a.name="B"
print(a.name)
del a.name
