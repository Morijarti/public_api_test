# pylint: disable=invalid-name, unused-argument
import django.test


def test_save_post_request(client: django.test.Client, db):
    response = client.post("/submit_abuse", data={"urls": "https://TEST.org"})
    assert response.status_code == 200
    assert "1" in response.content.decode()


def test_save_multiple_consecutive_post_request(client: django.test.Client, db):
    response = client.post("/submit_abuse", data={"urls": "https://TEST.org"})
    assert response.status_code == 200
    assert "1" in response.content.decode()

    response = client.post("/submit_abuse", data={"urls": "https://TEST1.org"})
    assert response.status_code == 200
    assert "2" in response.content.decode()
