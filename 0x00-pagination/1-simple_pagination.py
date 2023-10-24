#!/usr/bin/env python3
import csv
import pandas as pd
from typing import List

def index_range(page=3, page_size=15):
    if page < 1 or page_size < 1:
        return None  # Handle invalid input

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class BabyNamesDataset:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def get_page(self, page=1, page_size=10):
        if not (isinstance(page, int) and isinstance(page_size, int) and page > 0 and page_size > 0):
            return []  # Invalid input

        start, end = index_range(page, page_size)

        if start >= len(self.data):
            return []  # Page out of range

        return self.data.iloc[start:end].to_dict(orient='records')
