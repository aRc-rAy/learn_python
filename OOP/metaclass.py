class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        dct['custom_attribute'] = 'This is a custom attribute'
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    def __init__(self):
        self.data = "Hello, World!"

# Instantiate the class
obj = MyClass()
print(obj.data)
print(MyClass.custom_attribute)
