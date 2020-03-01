from mnmetro import GetDepartures

def test_departure_for():
    D = GetDepartures()
    data = D.departure_for(1000)

    assert data[0]["Description"] == "46St-42St/St. Paul-7St/Via Bryant"
            