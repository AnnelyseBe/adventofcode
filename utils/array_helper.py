import numpy as np
import warnings

class ArrayHelper:
    

    @staticmethod # Since the method does not use self or the class instance, it should be defined as a static method.    
    def find_next_coordinates_that_equal(my_array, item_to_search, start_index=(0, 0)):
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
    def find_next_coordinates_that_contain(my_array, item_to_search, start_index=(0, 0)):
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
        
    @staticmethod    
    def find_direction(source_position, destination_position):
        if (source_position[0] == destination_position[0] > 0): 
            if (source_position[1] == destination_position[1]):
                return None
            elif (source_position[1] - destination_position[1] > 0): # left
                return "w"
            else: # right
                return "e" 
        elif (source_position[0] - destination_position[0] > 0):   # up
            if (source_position[1] == destination_position[1]):
                return "n"
            elif (source_position[1] - destination_position[1] > 0): # left
                return "nw"
            else: # right
                return "ne"
        elif (source_position[0] - destination_position[0] < 0):   # down
            if (source_position[1] == destination_position[1]):
                return "s"
            elif (source_position[1] - destination_position[1] > 0): # left
                return "sw"
            else: # right
                return "se"
                

    @staticmethod
    def neighbour_coordinates(direction, position, only_return_valid = False, my_array = np.zeros(1)):
        """Gives neighbour coördinates. Validiy check is optional

        Args:
            direction (string): direction : "NORTH", "up", "^", "EAST", "right", ">", "SOUTH", "down", "v", "WEST", "left", "<",  
            direction : "NORTH", "up", "^", "EAST", "right", ">", "SOUTH", "down", "v", "WEST", "left", "<",  
            position (tuple): (row, column)
            only_return_valid: optional check for validity -> set True
            my_array: Optional, in case of validity check

        Returns:
            neighbour row , column. None when validity check is active and neighbour is not available
        """
        # Map directions to their corresponding row and column offsets
        direction_offsets = {
            "NORTH": (-1, 0), "north": (-1, 0), "n": (-1, 0), "up": (-1, 0), "^": (-1, 0),
            "EAST": (0, 1), "east": (0, 1), "e": (0, 1),"right": (0, 1), ">": (0, 1),
            "SOUTH": (1, 0), "south": (1, 0), "s": (1, 0), "down": (1, 0), "v": (1, 0),
            "WEST": (0, -1), "west": (0, -1), "w": (0, -1), "left": (0, -1), "<": (0, -1),  
        }
    
        # Get the offset for the specified direction
        offset = direction_offsets.get(direction)
    
        if not offset:  # Invalid direction, return current position
            return position

        # Calculate new position
        new_row, new_col = position[0] + offset[0], position[1] + offset[1]
        
        if(only_return_valid):
            # Check if the new position is within bounds
            if ArrayHelper.is_in_array_bounds(my_array, new_row, new_col):
                return new_row, new_col
            else:
                return None
            
        return position
        

    @staticmethod
    def valid_neighbour_coordinates_and_value(my_array, direction, position):
        """gives rownumber, columnnumber and value of the neighbour in a 2D numpy array. If the neighbour is not available, result will be None

        Args:
            my_array : 2D numpy array
            direction : "NORTH", "up", "^", "EAST", "right", ">", "SOUTH", "down", "v", "WEST", "left", "<",  
            position (tuple): (row, column)

        Returns:
            row_number, column_number, value
        """
        neighbour = ArrayHelper.neighbour_coordinates(direction, position, True, my_array)
        
        if (neighbour):
            new_row = neighbour[0]
            new_col = neighbour[1]
            return (new_row, new_col), my_array[new_row][new_col]

        # Return None if the position is out of bounds
        return None
    
    def print_2d_array_string_values(my_array, space_between_by=""):
        rows, cols = my_array.shape
        
        for row in range(rows):
            for col in range(cols):
                print(my_array[row, col], end =space_between_by)
            print('\n')
        
        
    
    @DeprecationWarning    
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
        

