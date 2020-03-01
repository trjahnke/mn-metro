from mnmetro import GetVehicleLocations

V = GetVehicleLocations()

def test_all_vehicles():
    data = V.all_vehicles()

    assert next(iter(data)) != None

def test_location_for():
    data = V.location_for(route_id=3)

    assert int(data[0]["Route"]) == 3
