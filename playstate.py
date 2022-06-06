class Animal:
    def __init__(self):
        self.num_eye = 2
    
    def breathe(Self):
        print('Inhale, exhale')


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("moving in water")
    
    def breathe(Self):
        super().breathe()
        print("doing under water")



nemo = Fish()
# nemo.swim()
nemo.breathe()
# print(nemo.num_eye)
    