from mnmetro import GetDirections

def test_direction_for():
    D = GetDirections()

    data = D.direction_for(3)

    assert data["EASTBOUND"] == 2