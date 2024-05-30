import pytest
import requests
from unittest.mock import patch


@pytest.fixture(scope="module")
def api_base_url():
    return "https://httpbin.org"

@pytest.fixture(params=["get", "post"])
def request_method(request):
    return request.param

@pytest.fixture(params=["/users", "/products"])
def api_endpoint(request):
    return request.param

@pytest.fixture
def auth_headers(request_method):
    if request_method == "post":
        return {"Authorization": "Bearer <token>"}
    else:
        return {}


@patch("requests.post")
@patch("requests.get")
def test_api_request(mock_get, mock_post, api_base_url, request_method, api_endpoint, auth_headers):
    url = api_base_url + api_endpoint
    headers = auth_headers

    # 模拟 API 响应
    mock_response = requests.Response()
    mock_response.status_code = 200

    # 配置模拟对象
    if request_method == "get":
        mock_get.return_value = mock_response
        response = requests.get(url, headers=headers)
    else:
        mock_post.return_value = mock_response
        response = requests.post(url, headers=headers, data={"key": "value"})

    assert response.status_code == 200
