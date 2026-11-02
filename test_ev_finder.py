from ev_finder import pick_cars

def test_cheap():
    assert pick_cars(15000) == "Chevy Bolt, Nissan Leaf"

def test_just_under_edge():
    assert pick_cars(59999) == "Ford F-150 Lightning, Rivian R1T"  

def test_edge_case():
    assert pick_cars(60000) == "Tesla Model S, Rivian R1S"      

def test_bold_edge():
    assert pick_cars(20000) <= "Tesla Model 3, Kia EV6"