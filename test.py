import re
import numpy as np


content= 'ljml_jmljlmllk_lk'
input_strings = re.split(r"(_)", content)
print(input_strings)

my_array = np.arange(1,31).reshape(6,5)
print(my_array)

my_diagonal = my_array.diagonal(offset=-1)
print(my_diagonal)


my_diagonal = my_array.diagonal(offset=-len(my_array)+1)
print(my_diagonal)


testset = {1,2,3}

print(testset.add(1))
print(testset.add(8))

