from mnmetro import GetProviders

P = GetProviders()

def test_all_providers():
    data = P.all_providers()

    assert data[8] == "Metro Transit"

def test_provider_for():
    data_id = P.provider_for(id=3)
    data_name = P.provider_for(name="SouthWest Transit")

    assert data_id == "Other" and data_name == 7
