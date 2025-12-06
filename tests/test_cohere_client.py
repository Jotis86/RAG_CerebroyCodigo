import pytest
from src.services.cohere_client import CohereClient

@pytest.fixture
def cohere_client():
    return CohereClient(api_key="test_api_key")

def test_send_message(cohere_client, mocker):
    mock_response = {"text": "Hello, how can I help you?"}
    mocker.patch("src.services.cohere_client.CohereClient.send_request", return_value=mock_response)

    response = cohere_client.send_message("Hi")
    assert response == "Hello, how can I help you?"

def test_send_message_error(cohere_client, mocker):
    mocker.patch("src.services.cohere_client.CohereClient.send_request", side_effect=Exception("API error"))

    with pytest.raises(Exception) as excinfo:
        cohere_client.send_message("Hi")
    assert str(excinfo.value) == "API error"