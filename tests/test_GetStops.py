from mnmetro import GetStops

S = GetStops()

def test_full_stops_for():
    data = S.full_stops_for(3)

    assert next(iter(data)) == "Eastbound"

def test_stops_for():
    data = S.stops_for(route_id=3, direction=2)

    assert next(iter(data)) != None
