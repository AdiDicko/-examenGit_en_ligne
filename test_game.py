from jeu import comparer

def test_trop_petit():
    assert comparer(50, 10) == "trop petit"

def test_trop_grand():
    assert comparer(50, 90) == "trop grand"

def test_gagne():
    assert comparer(50, 50) == "gagné"