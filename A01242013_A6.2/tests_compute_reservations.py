import unittest
from compute_reservations import ManageHotel, ManageReservation, ManageCustomer

class TestsComputeReservations(unittest.TestCase):
    hotel_file = 'Hotels.json'
    resrv_file = 'Reservations.json'
    customer_file = 'Customers.json'

    def setUp(self):
        self.hotel = ManageHotel(self.hotel_file)
        self.resrv = ManageReservation(self.resrv_file)
        self.customer = ManageCustomer(self.customer_file)

    def test_create_hotel_method_correct_result(self):
        h_id = 4
        h_name = "Hotel Maria Bonita"
        self.hotel.create_hotel(h_id, h_name)


if __name__ == '__main__':
    unittest.main()
    
    


