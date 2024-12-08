import numpy as np
import warnings

class ArrayHelper:
    

    @staticmethod # Since the method does not use self or the class instance, it should be defined as a static method.    
    def find_next_item_that_equals(my_array, item_to_search, start_index=(0, 0)):
        """
        Finds the position of a specific item in a 2D NumPy array, starting from a given index.

        Parameters:
        item_to_search: The item to search for in the array.
        start_index (tuple): The (row_index, column_index) to start searching from.

        Returns:
        tuple: A tuple of (row_index, column_index) if the item is found,
               (-1, -1) if the item is not found.
        """
        row_start, col_start = start_index
        rowcount, columncount = my_array.shape

        for rowindex in range(row_start, rowcount):
            for columnindex in range(col_start if rowindex == row_start else 0, columncount):
                if my_array[rowindex, columnindex] == item_to_search:
                    return rowindex, columnindex

        return -1, -1
    
    @staticmethod # Since the method does not use self or the class instance, it should be defined as a static method.
    def find_next_item_that_contains(my_array, item_to_search, start_index=(0, 0)):
        """
        Finds the position of a item in a 2D NumPy array that contains the item_to_search, starting from a given index.

        Parameters:
        item_to_search: The item to search for in the array. This item needs to be contained in the array element
        start_index (tuple): The (row_index, column_index) to start searching from.

        Returns:
        tuple: A tuple of (row_index, column_index) if the item is found,
               (-1, -1) if the item is not found.
        """
        row_start, col_start = start_index
        rowcount, columncount = my_array.shape

        for rowindex in range(row_start, rowcount):
            for columnindex in range(col_start if rowindex == row_start else 0, columncount):
                if item_to_search in my_array[rowindex, columnindex]:
                    return rowindex, columnindex

        return -1, -1
    
    @staticmethod # Since the method does not use self or the class instance, it should be defined as a static method.
    def is_in_array_bounds(my_array, row, column):
        rowcount, columncount = my_array.shape
        return row < rowcount and row >= 0 and column < columncount and column >= 0
    
    @staticmethod # Since the method does not use self or the class instance, it should be defined as a static method.
    def find_next_coordinate(my_array, row, column):
        rowcount, columncount = my_array.shape
        
        array_rank = row * columncount + column
        next_array_rank = array_rank + 1
        
        if (next_array_rank >= (rowcount * columncount)):
            return -1, -1
        else:
            return next_array_rank // columncount, next_array_rank % columncount
        
    @staticmethod # Since the method does not use self or the class instance, it should be defined as a static method.
    def find_item_position_in_2d(my_array, item_to_search):
        """
        Finds the position of a specific item in a 2D NumPy array.

        Parameters:
        my_array (np.ndarray): The 2D array to search in.
        item_to_search: The item to search for in the array.

        Returns:
        tuple: A tuple of (row_index, column_index) if the item is found,
               (-1, -1) if the item is not found.
        """
        
        warnings.warn(
            "this method is deprecated and will be removed in a future version. "
            "Use find_next_item_that_equals instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        rowcount, columncount = my_array.shape

        for rowindex in range(rowcount):
            for columnindex in range(columncount):
                if my_array[rowindex, columnindex] == item_to_search:
                    return rowindex, columnindex

        return -1, -1
        

