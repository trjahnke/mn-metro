from mnmetro import GetTimepointDepartures

T = GetTimepointDepartures()

def test_times_for():
    data = T.times_for(route_id=5, direction=4, node_id="7SOL")

    assert next(iter(data)) != None
