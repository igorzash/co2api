from src.conftest import client


def test_data_types(client):
    resp = client.simulate_get('/api/v1/distribution/dataTypes')

    assert resp.status_code == 200


def test_regions(client):
    resp = client.simulate_get('/api/v1/distribution/regions')

    assert resp.status_code == 200


def test_summary(client):
    resp = client.simulate_get('/api/v1/distribution/summary?year=2019&region=22&dataType=1')

    assert resp.status_code == 200
