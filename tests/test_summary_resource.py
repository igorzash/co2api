from src.conftest import client


def test_validate_params_on_nothing(client):
    resp = client.simulate_get('/api/v1/distribution/summary')

    assert resp.status_code == 400

def test_validate_params_on_invalid(client):
    resp = client.simulate_get('/api/v1/distribution/summary?year=2019&region=fa;fjsd;&dataType=1')

    assert resp.status_code == 400
    
    resp = client.simulate_get('/api/v1/distribution/summary?year=2019&region=fa;fjsd;&dataType=dfasd')

    assert resp.status_code == 400
    
    resp = client.simulate_get('/api/v1/distribution/summary?year=fasdfasf&region=fa;fjsd;&dataType=dfasd')

    assert resp.status_code == 400