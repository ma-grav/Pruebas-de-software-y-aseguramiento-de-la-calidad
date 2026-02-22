"""Program that tests Hotels and their inherent activities"""

import unittest
import json
from compute_reservations import ManageHotel, ManageReservation, ManageCustomer


def load_file(file_path):
    """Function to load a file"""
    with open(file_path, "r", encoding="utf-8") as f:
        file_dict = json.load(f)

    return file_dict


class TestsComputeReservations(unittest.TestCase):
    """Class to Test Compute Reservations"""
    hotel_file = 'Hotels.json'
    resrv_file = 'Reservations.json'
    customer_file = 'Customers.json'

    def setUp(self):
        """Function to setup for the testing"""
        self.hotel = ManageHotel(self.hotel_file)
        self.resrv = ManageReservation(self.resrv_file)
        self.customer = ManageCustomer(self.customer_file)

    def test_create_hotel_method_correct_result(self):
        """Function to test Create Hotel (Correct)"""
        h_id = 4
        h_name = "Hotel Maria Bonita"
        self.hotel.create_hotel(h_id, h_name)

        hotels_data = load_file(self.hotel_file)
        self.assertTrue(any(h['hotel_id'] == h_id for h in hotels_data))

    def test_delete_hotel_method_correct_result(self):
        """Function to test Delete Hotel (Correct)"""
        h_id = 3
        self.hotel.delete_hotel(h_id)

        hotels_data = load_file(self.hotel_file)
        self.assertFalse(any(h['hotel_id'] == h_id for h in hotels_data))

    def test_delete_hotel_method_incorrect_result(self):
        """Function to test Delete Hotel (Incorrect)"""
        h_id = 6
        self.hotel.delete_hotel(h_id)

        hotels_data = load_file(self.hotel_file)
        self.assertFalse(any(h['hotel_id'] == h_id for h in hotels_data))

    def test_display_hotel_method_correct_result(self):
        """Function to test Display Hotel (Correct)"""
        h_id = 4
        self.hotel.hotel_info(h_id)

        hotels_data = load_file(self.hotel_file)
        self.assertTrue(any(h['hotel_id'] == h_id for h in hotels_data))

    def test_display_hotel_method_incorrect_result(self):
        """Function to test Display Hotel (Incorrect)"""
        h_id = 6
        self.hotel.hotel_info(h_id)

        hotels_data = load_file(self.hotel_file)
        self.assertFalse(any(h['hotel_id'] == h_id for h in hotels_data))

    def test_modify_hotel_method_correct_result(self):
        """Function to test Modify Hotel (Correct)"""
        h_id = 1
        h_name = "Holiday Inn"
        self.hotel.modify_hotel(h_id, h_name)

        hotels_data = load_file(self.hotel_file)
        self.assertTrue(any(h['name'] == h_name for h in hotels_data))

    def test_create_customer_method_correct_result(self):
        """Function to test Create Customer (Correct)"""
        c_id = 4
        c_name = "Alicia Aguilar"
        c_email = "ali_aguilar16@gmail.com"
        self.customer.create_customer(c_id, c_name, c_email)

        customers_data = load_file(self.customer_file)
        self.assertTrue(any(c['customer_id'] == c_id for c in customers_data))

    def test_delete_customer_method_correct_result(self):
        """Function to test Delete Customer (Correct)"""
        c_id = 2
        self.customer.delete_customer(c_id)

        customers_data = load_file(self.customer_file)
        self.assertFalse(any(c['customer_id'] == c_id for c in customers_data))

    def test_delete_customer_method_incorrect_result(self):
        """Function to test Delete Customer (Incorrect)"""
        c_id = 2
        self.customer.delete_customer(c_id)

        customers_data = load_file(self.customer_file)
        self.assertFalse(any(c['customer_id'] == c_id for c in customers_data))

    def test_display_customer_method_correct_result(self):
        """Function to test Display Customer (Correct)"""
        c_id = 4
        self.customer.customer_info(c_id)

        customers_data = load_file(self.customer_file)
        self.assertTrue(any(c['customer_id'] == c_id for c in customers_data))

    def test_modify_customer_method_correct_result(self):
        """Function to test Modify Customer (Correct)"""
        c_id = 1
        c_name = "Ximena Aguilar"
        c_email = "ximena.flor15@gmail.com"
        self.customer.modify_customer(c_id, c_name, c_email)

        customers_data = load_file(self.customer_file)
        self.assertTrue(any(c['customer_name'] == c_name for
                            c in customers_data))

    def test_modify_customer_method_incorrect_result(self):
        """Function to test Modify Customer (Inorrect)"""
        c_id = 6
        c_name = "Paola Flores"
        c_email = "paopao.nuevo@outlook.com"
        self.customer.modify_customer(c_id, c_name, c_email)

        customers_data = load_file(self.customer_file)
        self.assertFalse(any(c['customer_name'] == c_name for
                             c in customers_data))

    def test_create_reservation_method_correct_result(self):
        """Function to test Create Reservation (Correct)"""
        r_id = 4
        r_room = "180"
        r_cus_id = 4
        r_hotel_id = 4
        self.resrv.new_reservation(r_id, r_room, r_cus_id, r_hotel_id)

        reservations_data = load_file(self.resrv_file)
        self.assertTrue(any(r['reservation_id'] == r_id for
                            r in reservations_data))

    def test_cancel_reservation_method_correct_result(self):
        """Function to test Cancel Reservation (Correct)"""
        r_id = 3
        self.resrv.cancel_reservation(r_id)

        reservations_data = load_file(self.resrv_file)
        self.assertFalse(any(r['reservation_id'] == r_id for
                             r in reservations_data))

    def test_cancel_reservation_method_incorrect_result(self):
        """Function to test Cancel Reservation (Incorrect)"""
        r_id = 6
        self.resrv.cancel_reservation(r_id)

        reservations_data = load_file(self.resrv_file)
        self.assertFalse(any(r['reservation_id'] == r_id for
                             r in reservations_data))


if __name__ == '__main__':
    unittest.main()
