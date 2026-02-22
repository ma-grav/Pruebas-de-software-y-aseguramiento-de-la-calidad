import argparse
from abc import ABC, abstractmethod

#pylint: disable=invalid-name

"Program that manages Hotels and their inherent activities"

#Hotel Classes 
class Hotel(ABC):

    @abstractmethod
    def to_dictionary(self):
        pass


class StandardHotel(Hotel):

    def __init__(self, hotel_id, name):
        self.hotel_id = hotel_id
        self.name = name 

    def to_dictionary(self):
        return self.__dict__
    

class ManageHotel:

    def create_hotel():
        pass 

    def delete_hotel():
        pass

    def hotel_info():
        pass

    def modify_hotel():
        pass


#Customer Classes 
class Customer:
    def __init__(self, customer_id, customer_name, customer_email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = customer_email

    def to_dictionary(self):
        return self.__dict__

class ManageCustomer:
     
    def create_customer():
        pass 

    def delete_customer():
        pass

    def customer_info():
        pass

    def modify_customer():
        pass


#Reservation Classes 
class Reservation(ABC):

    @abstractmethod
    def to_dictionary(self):
        pass


class RoomReservation(Reservation):

    def __init__(self, reservation_id, room_num, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.room_num = room_num
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dictionary(self):
        return self.__dict__
    

class ManageReservation:

    def new_reservation():
        pass 

    def cancel_reservation():
        pass