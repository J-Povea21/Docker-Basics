# In this file is stored the bloom filter implementation!

"""
This implementation of the bloom filter is based on the following article:
https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
"""



# Imports
import math
import mmh3
from bitarray import bitarray
from typing import Any


class BloomFilter:

    def __init__(self, items_number: int, false_positive_prob: float) -> None:
        self.fp_prob = false_positive_prob

        self.size = self.get_barray_size(items_number, false_positive_prob)

        self.hash_count = self.get_hash_count(self.size, items_number)

        # Here we create the array of bits
        self.bit_array = bitarray(self.size)

        # We set all the elements of the array to zero
        self.bit_array.setall(0)

    def add(self, item: Any) -> None:
        indexes = []

        for i in range(self.hash_count):
            # The hash fn returns a certain index
            index = mmh3.hash(item, i) % self.size
            indexes.append(index)

            # Set the bit to true in the bit array
            self.bit_array[index] = True

    def check_existence(self, item: Any) -> bool:

        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size

            if not self.bit_array[index]:
                return False

        return True

    @staticmethod
    def get_barray_size(number_items: int, fp_prob: float) -> int:
        # This functions uses the following formula in order to get the size of the bit array
        bit_size = -(number_items * math.log(fp_prob)) / (math.log(2) ** 2)

        return int(bit_size)

    @staticmethod
    def get_hash_count(barray_size, number_items) -> int:
        k = (barray_size / number_items) * math.log(2)
        return int(k)
