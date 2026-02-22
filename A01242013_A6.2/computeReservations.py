import argparse
from abc import ABC, abstractmethod
import json

#pylint: disable=invalid-name

"Program that manages Hotels and their inherent activities"

def load_file(file):
    with open(input_file.file, "r", encoding="utf-8") as f:
        file_dict = json.load(f)
    
    return file_dict

def save_file(d):
    with open(input_file.file, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)


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

    def __init__(self, f):
        self.FILE = f

    def create_hotel(self, new_hotel):
        hotels_data = load_file(self.FILE)
        hotels_data.append(new_hotel)
        save_file(self.FILE, hotels_data)


    def delete_hotel(self, hotel_name):
        hotels_data = load_file(self.FILE)
        
        for x in hotels_data:
            hotel_exists = any(x['name'] == hotel_name for hotel in hotels_data)

            if hotel_exists:
               if x['name'] == hotel_name:
                    hotels_data.pop(x)
            else:
                print(f"Hotel {hotel_name} does not exist.")

        save_file(self.FILE, hotels_data)

    def hotel_info(self, hotel_name):
        hotels_data = load_file(self.FILE)
        
        for x in hotels_data:
            hotel_exists = any(x['name'] == hotel_name for hotel in hotels_data)

            if hotel_exists:
               if x['name'] == hotel_name:
                    print(x)
            else:
                print(f"Hotel {hotel_name} does not exist.")

        save_file(self.FILE, hotels_data)
        

    def modify_hotel(self, hotel_id, new_hotel_name):
        hotels_data = load_file(self.FILE)
        
        for x in hotels_data:
            hotel_exists = any(x['id'] == hotel_id for hotel in hotels_data)

            if hotel_exists:
               if x['id'] == hotel_id:
                    hotels_data.update({'name': new_hotel_name})
            else:
                print(f"Hotel {hotel_id} does not exist.")

        save_file(self.FILE, hotels_data)


#Customer Classes 
class Customer:
    
    def __init__(self, customer_id, customer_name, customer_email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = customer_email

    def to_dictionary(self):
        return self.__dict__

class ManageCustomer:

    def __init__(self, f):
        self.FILE = f

    def create_customer(self, new_cust):
        cust_data = load_file(self.FILE)

        cust_data.append()
        save_file(self.FILE, cust_data)

    def delete_customer(self, cust_id):
        cust_data = load_file(self.FILE)
        
        for x in cust_data:
            cust_exists = any(x['customer_id'] == cust_id for customer in cust_data)

            if cust_exists:
               if x['customer_id'] == cust_id:
                    cust_data.pop(x)
            else:
                print(f"Customer {cust_id} does not exist.")

        save_file(self.FILE, cust_data)

    def customer_info(self, cust_id):
        cust_data = load_file(self.FILE)
        
        for x in cust_data:
            cust_exists = any(x['customer_id'] == cust_id for customer in cust_data)

            if cust_exists:
               if x['customer_id'] == cust_id:
                    print(x)
            else:
                print(f"Customer {cust_id} does not exist.")

        save_file(self.FILE, cust_data)

    def modify_customer(self, cust_id, new_name, new_email):
        cust_data = load_file(self.FILE)
        
        for x in cust_data:
            cust_exists = any(x['customer_id'] == cust_id for customer in cust_data)

            if cust_exists:
               if x['customer_id'] == cust_id:
                    cust_data.cust_data.update({'customer_name': new_name}, {'email': new_email})
            else:
                print(f"Customer {cust_id} does not exist.")

        save_file(self.FILE, cust_data)


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

    def __init__(self, f):
        self.FILE = f

    def new_reservation(self, new_resrv):
        pass

    def cancel_reservation():
        pass



parser = argparse.ArgumentParser(description="Process hotel files")
parser.add_argument("hotel_file", help="Name of the hotels file")
parser.add_argument("reserv_file", help="Name of the reservations file")
parser.add_argument("customer_file", help="Name of the customers file")

input_file = parser.parse_args()

hotel_admin = ManageHotel(input_file.hotel_file)
reserv_admin = ManageReservation(input_file.reserv_file)
cust_admin = ManageCustomer(input_file.customer_file)




