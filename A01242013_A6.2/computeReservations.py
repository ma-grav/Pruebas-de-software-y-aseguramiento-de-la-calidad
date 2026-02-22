import argparse
from abc import ABC, abstractmethod

#pylint: disable=invalid-name

"Program that manages Hotels and their inherent activities"


class Hotel(ABC):

    @abstractmethod
    def to_dictionar(self):
        pass



