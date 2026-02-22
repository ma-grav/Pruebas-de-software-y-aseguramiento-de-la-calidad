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
    


