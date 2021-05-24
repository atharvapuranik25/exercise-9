class MedPlus:
    def __init__(self, name, batch, price):
        self.name = name
        self.batch = batch
        self.price = price
    def medicine(self):
        print("Name of medicine: ", self.name)
        print("Batch no.: ", self.batch)
        print("Price: ", self.price)

name = str(input("Name of medicine: "))
batch = int(input("Batch no.: "))
price = float(input("Price: "))

med1 = MedPlus(name, batch, price)
med1.medicine()
