
import pytest
import logging


TEST_NAME = "test1"
LOGGER = logging.getLogger(__name__)
from utils.excel_utils import read_xlsx_file
from utils.url_response import UrlResponse


class SharedGlobal:
    output = read_xlsx_file(TEST_NAME)
    test_names = list(output.keys())
    test_data = output


@pytest.mark.parametrize("test_name", SharedGlobal.test_names)
def test_verify_get_request(test_name):
    test = SharedGlobal.test_data[test_name]
    LOGGER.info(test['test_name'])
    response = UrlResponse(test['url']).response
    for k, v in test.items():
        if 'test_name' in k or 'url' in k:
            continue
        assert str(response[k]) == str(v)

"""
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = UrlResponse(url)

    expected_response = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }

    response = requests.get(url)
    LOGGER.info("Test is running")
    assert response.status_code == 200
    assert response.json() == expected_response
"""
"""
def test_verify_response_length():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    expected_length = 4

    response = requests.get(url)
    assert response.status_code == 200
    response_length = len(response.json())
    assert len(response.json()) == expected_length
"""