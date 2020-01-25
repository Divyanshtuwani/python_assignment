from automobile import Automobile
class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        self.__doors=doors
        Automobile.__init__(self,make,model,mileage,price)
    def set_doors(self,doors):
        self.__doors=doors
    def get_doors(self):
        return self.__doors
class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        self.__drive_type=drive_type
        Automobile.__init__(self,make,model,mileage,price)
    def set_drive_type(self,drive_type):
        self.__drive_type=drive_type
    def get_drive_type(self):
        return self.__drive_type
class SUV(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        self.__pass_cap=pass_cap
        Automobile.__init__(self,make,model,mileage,price)
    def set_pass_cap(self,pass_cap):
        self.__pass_cap=pass_cap
    def get_pass_cap(self):
        return self.__pass_cap
def main():
    c=Car('1','2','3','4','5')
    print("make",c.get_make())
    print("model",c.get_model())
    print("mileage",c.get_mileage())
    print("price",c.get_price())
    print("doors",c.get_doors())
    print()
    t=Truck('9','8','7','6','5')
    print("make",t.get_make())
    print("model",t.get_model())
    print("mileage",t.get_mileage())
    print("price",t.get_price())
    print("drive_type",t.get_drive_type())
    print()
    s=SUV('2','4','6','8','10')
    print("make",s.get_make())
    print("model",s.get_model())
    print("mileage",s.get_mileage())
    print("price",s.get_price())
    print("pass_cap",s.get_pass_cap())
main()
