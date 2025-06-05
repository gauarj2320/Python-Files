class Test:
    def __init__(self,name): # constructor
        self.name=name
        print(f"Constructor executed for {self.name} object")

t1=Test('t1') # object creation
t2=Test('t2')
t3=Test('t3')
t1.__init__('t1') # Constructor can also be called explicitly like a normal method also

#Constructor:
# Used to declare and initialise instance variable
# get automatically  call and execute when an object is created
# must have atleat one argument that is self