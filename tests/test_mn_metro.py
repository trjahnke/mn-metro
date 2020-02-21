from mn_metro import GetProviders

def test_providers():
    providers = GetProviders()
    response = providers.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396