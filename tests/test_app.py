import pytest
from io import BytesIO
from src.app import app, allowed_file
from tests.test_data.test_data import TEST_DATA

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("file_info", TEST_DATA)
def test_allowed_file(file_info):
    assert allowed_file(file_info["file"]) == file_info["allowed_file"]

def test_no_file_in_request(client):
    response = client.post("/classify_file")
    assert response.status_code == 400

def test_no_selected_file(client):
    data = {"file": (BytesIO(b""), "")}
    response = client.post("/classify_file", data=data, content_type="multipart/form-data")
    assert response.status_code == 400

@pytest.mark.parametrize("file_info", TEST_DATA)
def test_success(client, file_info):
    data = {
        "file": (file_info["file"], file_info["file"].filename)
    }
    response = client.post("/classify_file", data=data, content_type="multipart/form-data")

    print(response)

    assert response.status_code == 200
    assert response.get_json() == {"file_class": file_info["document_class"]}


    # mocker.patch("src.app.classify_file", return_value="test_class")

    # data = {"file": (BytesIO(b"dummy content"), "file.pdf")}
    # response = client.post("/classify_file", data=data, content_type="multipart/form-data")
    # assert response.status_code == 200
    # assert response.get_json() == {"file_class": "test_class"}