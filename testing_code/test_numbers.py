import numpy as np
from numpy.testing import assert_almost_equal
import numexpr as ne

def test_numpy():
    x = np.linspace(0, 5, 100)
    result1 = x**3
    result2 = x*x*x
    assert_almost_equal(result1, result2)
    
def test_numexpr():
    x = np.linspace(0, 5, 100)
    result1 = x**3
    result2 = ne.evaluate("x**3")
    assert_almost_equal(result1, result2)