class Person: 
    def __init__(self, name): 
        self.name= name
        print("Person intialized")

class Order: 
    def __init__(self,order_id): 
        self.order_id = order_id
        print("Order intialized")
#child  combing both(muliple iheritance )
class Customer(Person,Order):
    def __init__(self,name,order_id):
    
        print("coustomer called")

        super().__init__(name)
        Order.__init__(self,order_id)


        print(f" customer created:{self,name},Order:{self.order_id}")

class PrimeCustomer(Customer): 
    def __init__(self,name,order_id,prime_level): 
        super().__init__(name,order_id)

        self.prime_level= prime_level

        print(f"Prime Cusomer level:{self.prime_level}")

p1 = PrimeCustomer("VEnkat",4567, "Gold")
print(p1.name)
print(p1.order_id)
print(p1.prime_level)



            






