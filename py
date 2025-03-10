class Personal:   # give your Height and Weight
    
    def __init__(self,height:int,weight:int)->None:
        self.x=height
        self.y=weight
    def __iter__(self):
        
        return (i for i in (self.x ,self.y))
    
    def for_loop(self):
        result=[]
        for i in (self.x, self.y):
            result.append(i)
            if i < 145 and i < 49: 
                print('your not accept '.capitalize())
                break    
            return f'your value in list {result}'
    def __repr__(self):
        return f'{self.__class__.__name__} and {self.x, self.y}'   
    # def __str__(self)->int:
    #     return f' your number is {self.x} two numebr is {self.y}'
z=Personal(1,3)
#print(f'your name class is {Personal.__name__}', repr(z))
num=z.for_loop()
print(num)
