""" Test BerryDataFetcher """
from unittest.mock import Mock
import pytest
from app.berries.berry_data_fetcher import BerryDataFetcher

def test_berry_data_fetcher_inicialization(mocker):
    """ Test Inicialization of BerryDataFetcher"""

    expected_url = "https://pokeapi.co/api/v2/berry"
    mocker.patch("os.getenv", return_value=expected_url)
    fetcher = BerryDataFetcher()
    assert fetcher.all_data


@pytest.mark.parametrize("url, expected_data", [
    ("https://example.com/api/v2/berry", {
        "results": [{"name": "test_berry"}], "next": None
    }),
    ("https://example.com/api/v2/berry?page=2", {
        "results": [{"name": "test_berry_2"}], "next": None
    })
])
def test_fetch_data(url, expected_data, monkeypatch):
    """ Test Fetch Data """
    mock_response = Mock(json=lambda: expected_data)
    monkeypatch.setattr("requests.get", lambda url, timeout=30: mock_response)

    fetcher = BerryDataFetcher()
    data = fetcher.fetch_data(url)
    assert data == expected_data
