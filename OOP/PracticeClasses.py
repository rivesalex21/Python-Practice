# Purpose of this script is to gain some experience using the classes within Python. 
'''
1) Class creation;
2) Creating methods and atributes within classes
3) Creating class methods within the class
4) Using special attributes such as __add__, __str__ , __repr__,
5) Creating getter, setter, and static methods within the class.
6) Creating sub classes
'''

# Part One: Let us create a class, we'll make it a car class.


class BasicCar:
    wheels = 4;

    def __init__(self, make, model, year):
        self.make = make;
        self.model = model;
        self.year = year;


class LuxuryCar(BasicCar):

    def __init__(self, make, model, year, cost, tier, leather):
        super().__init__(make,model,year)
        self.cost = cost;
        self.tier = tier;
        self.leather = leather;

Lexus = LuxuryCar('Lexus','gs350',2020,45000,8,True)
print(Lexus.tier)