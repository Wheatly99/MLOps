from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_upload_file():
    test_file = 'test/data.xlsx'
    files = {'file': ('test/data.xlsx', open(test_file, 'rb'))}
    response = client.post('/file', files=files)
    json_data = response.json()
    assert response.status_code == 200
    assert json_data <= 5