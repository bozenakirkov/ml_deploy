

def test_app(client):
    res = client.get("/apidocs/", data={"input_file": '../tests/test_data/test_image_1000.npz'})
    assert res.status_code == 200


