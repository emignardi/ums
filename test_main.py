from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from main import app, get_db

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/ums_test")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def setup():
    post_response = client.post("/users", json={"first_name": "John", "last_name": "Denver", "email": "jdenver@outlook.com", "phone": "9059042920", "address": "101 Starwood Drive"})

def test_read(setup):
    get_response = client.get("/users")
    assert get_response.status_code == 200
    assert get_response.json() == [{"id": 1, "first_name": "John", "last_name": "Denver", "email": "jdenver@outlook.com", "phone": "9059042920", "address": "101 Starwood Drive"}]

def test_create():
    post_response_2 = client.post("/users", json={"first_name": "Bob", "last_name": "Dylan", "email": "visions@gmail.com", "phone": "9053049182", "address": "123 Nowhere Lane"})
    data = post_response_2.json()
    id = data["id"]
    assert post_response_2.status_code == 201
    assert post_response_2.json() == {"id": id, "first_name": "Bob", "last_name": "Dylan", "email": "visions@gmail.com", "phone": "9053049182", "address": "123 Nowhere Lane"}

def test_read_by_id(setup):
    get_response = client.get("/users/1")
    assert get_response.status_code == 200
    assert get_response.json() == {"id": 1, "first_name": "John", "last_name": "Denver", "email": "jdenver@outlook.com", "phone": "9059042920", "address": "101 Starwood Drive"}

def test_update(setup):
    put_response = client.put("/users/1", json={"first_name": "John", "last_name": "Deutschendorf", "email": "jdenver@outlook.com", "phone": "9059042920", "address": "101 Starwood Drive"})
    assert put_response.status_code == 200
    assert put_response.json() == {"id": 1, "first_name": "John", "last_name": "Deutschendorf", "email": "jdenver@outlook.com", "phone": "9059042920", "address": "101 Starwood Drive"}

def test_delete(setup):
    delete_response = client.delete("/users/1")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"id": 1, "first_name": "John", "last_name": "Deutschendorf", "email": "jdenver@outlook.com", "phone": "9059042920", "address": "101 Starwood Drive"}
    response = client.get("/users/1")
    assert response.status_code == 404