import pandas
from abc import ABC, abstractmethod #abc is module and ABC is a class # abstract base class

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "the real state company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
    @classmethod
    def get_hotel_count(cls, data): # clas/self is just a variable
        return len(data)

    # magic methods
    def __eq__(self, other): # comparing self and other variables. We overwrites eq method
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

    # can make many magic methods
    # def __add__(self, other):
    #     total = self.price + other.price
    #     return total


class Ticket(ABC):     # to define some rules, to make code more clearer and alos let other programmers know that
                       # whatever methods are inside abstract method , they have to add these methods inside other classes , in this case its generate() method
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property # property behaves like variable
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod # its like a function, used when here if we want to convert price to euroes
    def convert(amount):
        return amount * 1.2

class DigitalTicket(Ticket):
    def generate(self):
        return "Hello, this is your digital ticket"

hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.available()) # instance method [T/F]

print(hotel1.name)  # hotel1 is instance variable , self holds hotel1
print(hotel2.name)

print(hotel1.watermark) # watermark is class variable, can share its values with every variable
print(hotel2.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df)) # class method are universal and access from instances also
print(hotel1.get_hotel_count(data=df))


ticket = ReservationTicket(customer_name="john smith", hotel_object=hotel1)
print(ticket.customer_name)
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)

# hotel1 == hotel2 is False, they are two different instances
# "188" == "188" is True , so we can overwrite == (__eq__) method