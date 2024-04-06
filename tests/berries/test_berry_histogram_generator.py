""" Testing class HistogramGenerator """
# pylint: disable=W0621
import pytest
from app.berries.histogram_generator import HistogramGenerator

@pytest.fixture
def mock_berry_statistics(mocker):
    """ Mock Fixture to use in differnt cases """
    mock = mocker.patch('app.berries.berry_statistics.BerryStatistics')
    mock.growth_times = [3, 6, 9, 10, 12]
    mock.min_growth_time = 3
    mock.max_growth_time = 12

    return mock

def test_histogram_generator_initilization(mock_berry_statistics):
    """ Test init of HistogramGenerator """
    histogram_generator = HistogramGenerator(mock_berry_statistics)
    assert isinstance(histogram_generator, HistogramGenerator)


def test_histogram_generator_generate_histogram(mock_berry_statistics, tmp_path):
    """ Test generate histogram png """
    histogram_generator = HistogramGenerator(mock_berry_statistics)
    histogram_generator.generate_histogram(imgs_path=tmp_path)

    file_name = "histogram.png"
    histogram_path = tmp_path / file_name

    assert histogram_path.exists(), f"File {file_name} has not been created"
