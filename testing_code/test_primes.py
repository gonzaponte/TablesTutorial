def is_prime(number):
    """Return True if *number* is prime."""
    if (number <= 0):
        raise ValueError("Negative numbers or 0 not allowed")
    if (round(number) != number):
        raise ValueError("This functions is for integers only")
    if number == 1: return False
    
    
    for element in range(2,number):
        if number % element == 0:
            return False
    return True

def test_is_five_prime():
    """Is five successfully determined to be prime?"""
    assert is_prime(5)
    
def test_is_ten_prime():
    """Is five successfully determined to be prime?"""
    assert not is_prime(10)

def test_is_one_prime():
    """Is five successfully determined to be prime?"""
    assert not is_prime(1)
    
def test_is_negative_prime():
    """Is five successfully determined to be prime?"""
    try:
        is_prime(-10)
    except ValueError:
        return True
        