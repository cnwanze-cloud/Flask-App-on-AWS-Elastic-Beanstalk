from application import application


def test_home_returns_200():
    client = application.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Elastic Beanstalk" in response.data


def test_health_endpoint():
    client = application.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}