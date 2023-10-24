import csv
import math
from typing import List

def index_range(page, page_size):
    if page < 1 or page_size < 1:
        return None  # Handle invalid input

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class BabyNamesDataset:
    def __init__(self, csv_file):
        self.data = []
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)

    def get_page(self, page=1, page_size=10):
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start, end = index_range(page, page_size)
        if start >= len(self.data):
            return []  # Page out of range

        return self.data[start:end]
