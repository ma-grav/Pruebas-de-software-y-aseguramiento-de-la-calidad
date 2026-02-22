"""Program that manages Hotels and their inherent activities"""

from abc import ABC, abstractmethod
import json

# pylint: disable=too-few-public-methods


def load_file(file_path):
    """Function to load a file, used in multiple classes"""
    with open(file_path, "r", encoding="utf-8") as f:
        file_dict = json.load(f)

    return file_dict


def save_file(file_path, d):
    """Function to save a file, used in multiple classes"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)


# Hotel Classes
class Hotel(ABC):
    """Abstract class for hotels"""
    @abstractmethod
    def to_dictionary(self):
        """Function to return its own dictionary"""


class StandardHotel(Hotel):
    """Class that handles the methods needed for a standard hotel"""
    def __init__(self, hotel_id, name):
        self.hotel_id = hotel_id
        self.name = name

    def to_dictionary(self):
        return self.__dict__


class ManageHotel:
    """Class that handles the methods to manage the hotels data"""
    def __init__(self, f):
        self.file = f

    def create_hotel(self, h_id, name):
        """Function create a new hotel"""
        new_hotel = {"hotel_id": h_id, "name": name}
        hotels_data = load_file(self.file)
        hotels_data.append(new_hotel)
        save_file(self.file, hotels_data)

    def delete_hotel(self, hotel_id):
        """Function delete a hotel"""
        hotels_data = load_file(self.file)

        hotel_exists = any(h['hotel_id'] == hotel_id for h in hotels_data)

        if hotel_exists:
            for x in enumerate(hotels_data):

                if hotels_data[x]['hotel_id'] == hotel_id:
                    hotels_data.pop(x)
                break
        else:
            print(f"Customer {hotel_id} does not exist.")

        save_file(self.file, hotels_data)

    def hotel_info(self, hotel_name):
        """Function to print the information from a hotel"""
        hotels_data = load_file(self.file)

        hotel_exists = any(h['name'] == hotel_name for h in hotels_data)

        if hotel_exists:
            for x in enumerate(hotels_data):

                if hotels_data[x]['name'] == hotel_name:
                    print(x)
                break
        else:
            print(f"Customer {hotel_name} does not exist.")

    def modify_hotel(self, hotel_id, new_hotel_name):
        """Function modify a hotel's data"""
        hotels_data = load_file(self.file)

        hotel_exists = any(h['hotel_id'] == hotel_id for h in hotels_data)

        if hotel_exists:
            for x in enumerate(hotels_data):

                if hotels_data[x]['hotel_id'] == hotel_id:
                    hotels_data[x].update({"name": new_hotel_name})
                break
        else:
            print(f"Customer {hotel_id} does not exist.")

        save_file(self.file, hotels_data)


# Customer Classes
class Customer:
    """Class that handles the methods needed for the customers"""
    def __init__(self, customer_id, customer_name, customer_email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = customer_email

    def to_dictionary(self):
        """Function to return its own dictionary"""
        return self.__dict__


class ManageCustomer:
    """Class that handles the management of the customers data"""
    def __init__(self, f):
        self.file = f

    def create_customer(self, c_id, name, email):
        """Function create a new customer"""
        new_cust = {"customer_id": c_id, "customer_name": name, "email": email}
        cust_data = load_file(self.file)
        cust_data.append(new_cust)
        save_file(self.file, cust_data)

    def delete_customer(self, cust_id):
        """Function to delete a customer"""
        cust_data = load_file(self.file)

        cust_exists = any(c['customer_id'] == cust_id for c in cust_data)

        if cust_exists:
            for x in enumerate(cust_data):

                if cust_data[x]['customer_id'] == cust_id:
                    cust_data.pop(x)
                break
        else:
            print(f"Customer {cust_id} does not exist.")

        save_file(self.file, cust_data)

    def customer_info(self, cust_id):
        """Function to print a customer's data"""
        cust_data = load_file(self.file)

        cust_exists = any(c['customer_id'] == cust_id for c in cust_data)

        if cust_exists:
            for x in enumerate(cust_data):

                if cust_data[x]['customer_id'] == cust_id:
                    print(x)
                break
        else:
            print(f"Customer {cust_id} does not exist.")

    def modify_customer(self, cust_id, new_name, new_email):
        """Function to modify a customer's data"""
        cust_data = load_file(self.file)

        cust_exists = any(c['customer_id'] == cust_id for c in cust_data)

        if cust_exists:
            for x in enumerate(cust_data):

                if cust_data[x]['customer_id'] == cust_id:
                    cust_data[x].update({"customer_name": new_name,
                                        "email": new_email})
                break
        else:
            print(f"Customer {cust_id} does not exist.")

        save_file(self.file, cust_data)


# Reservation Classes
class Reservation(ABC):
    """Abstract class for reservations"""
    @abstractmethod
    def to_dictionary(self):
        """Function to return its own dictionary"""


class RoomReservation(Reservation):
    """Class that handles the methods needed for a room reservation"""
    def __init__(self, reservation_id, room_num, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.room_num = room_num
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dictionary(self):
        return self.__dict__


class ManageReservation:
    """Class that handles the mmanagement of the reservations data"""
    def __init__(self, f):
        self.file = f

    def new_reservation(self, resrv_id, room, cust_id, hotel_id):
        """Function to create a new reservation"""
        new_resrv = {"reservation_id": resrv_id, "room_num": room,
                     "customer_id": cust_id, "hotel_id": hotel_id}
        resrv_data = load_file(self.file)
        resrv_data.append(new_resrv)
        save_file(self.file, resrv_data)

    def cancel_reservation(self, resrv_id):
        """Function to cancel a reservation, in this case it is deleted"""
        resrv_data = load_file(self.file)

        resrv_exists = any(r['reservation_id'] == resrv_id for r
                           in resrv_data)

        if resrv_exists:
            for x in enumerate(resrv_data):

                if resrv_data[x]['hotel_id'] == resrv_id:
                    resrv_data.pop(x)
                break
        else:
            print(f"Customer {resrv_id} does not exist.")

        save_file(self.file, resrv_data)
