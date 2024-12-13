class Manufacturer:
    def __init__(self,identity,location):
        self.identity = identity
        self.location = location
    
    #getter
    def get_identity(self):
        return self.identity
    def get_location(self):
        return self.location
    
    #setter
    def set_identity(self,identity):
        self.identity = identity
    def set_location(self,location):
        self.location = location
    
    #describe()
    def describe(self):
        print(f"identity= {self.identity}, location= {self.location}")

class Device(Manufacturer):

    def __init__(self,name,price,identity,location):
        super().__init__(identity,location)
        self.name = name
        self.price = price
    
    #getter
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

    #setter
    def set_name(self,name):
        self.name = name 
    def set_price(self,price):
        self.price = price
    
    #desrcibe
    def describe(self):
        print(f"name= {self.name}, price= {self.price}", end= ", ")
        super().describe()
    
device1 = Device(name="mouse",price=2.5,identity=9725,location="Vietnam")
device1.describe()
device2 = Device(name="monitor",price=12.5,identity=11,location="Germany")
device2.describe()



