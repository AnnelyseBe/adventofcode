import numpy as np

class ArrayHelper:
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
        rowcount, columncount = my_array.shape

        for rowindex in range(rowcount):
            for columnindex in range(columncount):
                if my_array[rowindex, columnindex] == item_to_search:
                    return rowindex, columnindex

        return -1, -1
        

