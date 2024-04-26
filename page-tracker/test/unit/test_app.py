# import pytest
import pytest
import unittest.mock
from redis import ConnectionError

from page_tracker.app import app

# use the decorator @fixture. Decorator allow you to modify or extend the behaviour of functions or methods whithout changing their actual code.


@pytest.fixture
def http_client():
    return app.test_client()

# wrap the test function with Python @patch decorator to inject a mocked Redis client into it as an argument

# given/when/then -> behaviour-driven


@unittest.mock.patch("page_tracker.app.redis")
def test_should_call_redis_incr(mock_redis, http_client):
    # given
    # always return 5 whenever its .incr() method gets called.
    mock_redis.return_value.incr.return_value = 5

    # when
    # check the server's response status and body
    response = http_client.get("/")

    # then
    assert response.status_code == 200
    assert response.text == "This page has been seen 5 times"
    mock_redis.return_value.incr.assert_called_once_with("page_views")
