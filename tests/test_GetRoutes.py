from mnmetro import GetRoutes

R = GetRoutes()

def test_all_routes():
    data = R.all_routes()

    assert len(data) == 70

def test_route_ids():
    data = R.route_ids()

    assert data[0] == 2

def test_route_for():
    data = R.route_for(3)

    assert data["Route"] == 3