import pytest
import numpy as np
from utils.array_helper import ArrayHelper

@pytest.fixture
def sample_matrix():
    test_matrix = np.arange(0,144).reshape((6,-1))
    print(test_matrix.shape)
    return test_matrix

def test_is_in_array_bounds(sample_matrix): 
    assert ArrayHelper.is_in_array_bounds(sample_matrix, 15, 12) is False
    
def test_unittests():
    assert False is True