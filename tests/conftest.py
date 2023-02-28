import pytest
from poetrytest.app import app as my_app


@pytest.fixture
def app():
    my_app.config.update({
        "TESTING": True,
    })
    yield my_app


@pytest.fixture
def client(app):
    return app.test_client()

