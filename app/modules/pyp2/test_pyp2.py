from flask import url_for
from pytest import approx

def test_hexgrid(client):
    response = client.get("/api/v1/pyp2/hexgrid/")
    assert response.status_code == 200
    assert len(response.json["features"]) == 1098