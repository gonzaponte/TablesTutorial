def calc_gc(sequence):
    sequence = sequence.upper()                    # make all chars uppercase
    n = sequence.count('T') + sequence.count('A')  # count only A, T,
    m = sequence.count('G') + sequence.count('C')  # C, and G -- nothing else (no Ns, Rs, Ws, etc.)
    return float(m) / float(n + m) if n+m else 0

def test_1(): # test handling N
    result = round(calc_gc('NATGC'), 2)
    assert result == 0.5, result
    
def test_2(): # test handling lowercase
    result = round(calc_gc('natgc'), 2)
    assert result == 0.5, result