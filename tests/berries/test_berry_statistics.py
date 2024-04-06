""" Testing BerryStatistics class """
# pylint: disable=W0621
import pytest
from app.berries.berry_statistics import BerryStatistics


@pytest.fixture
def mock_berry_data_fetcher(mocker):
    """ Mock of class BerryDataFetcher """
    mock = mocker.patch('app.berries.berry_data_fetcher.BerryDataFetcher')
    mock.all_data = [
        { "name": "micle", "url": "https://pokeapi.co/api/v2/berry/61/"},
        { "name": "custap", "url": "https://pokeapi.co/api/v2/berry/62/"},
        { "name": "jaboca", "url": "https://pokeapi.co/api/v2/berry/63/"},
    ]

    return mock

def test_berry_statistics_initialization(mock_berry_data_fetcher):
    """ Test BerryStatistics Instance """
    berry_statistics = BerryStatistics(mock_berry_data_fetcher)
    assert isinstance(berry_statistics, BerryStatistics)


def test_berry_statistics_properties(mock_berry_data_fetcher, mocker):
    """ Test Berry Peroperties """
    mocker.patch.object(
        BerryStatistics, 'get_berry_growth_times', return_value=[3, 6, 9]
    )

    berry_statistics = BerryStatistics(mock_berry_data_fetcher)

    assert berry_statistics.berries_names == ['micle', 'custap', 'jaboca']
    assert berry_statistics.min_growth_time == 3
    assert berry_statistics.max_growth_time == 9


def test_berry_statistics_get_stats_response(mock_berry_data_fetcher, mocker):
    """ Test Stats """
    mocker.patch.object(
        BerryStatistics, 'get_berry_growth_times', return_value=[3, 6, 9]
    )

    berry_statistics = BerryStatistics(mock_berry_data_fetcher)
    stats = berry_statistics.get_stats()
    assert 'berries_names' in stats
    assert 'min_growth_time' in stats
    assert 'median_growth_time' in stats
    assert 'max_growth_time' in stats
    assert 'variance_growth_time' in stats
    assert 'mean_growth_time' in stats
    assert 'frequency_growth_time' in stats
