#!/usr/bin/env python3
def index_range(page, page_size):
    if page < 1 or page_size < 1:
        return None  # Handle invalid input

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
