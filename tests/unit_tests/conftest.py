import pytest
import pytest_socket


# disables all real socket calls to suppress network access
# to enable it for a specific test, use @pytest.mark.enable_socket
def pytest_runtest_setup():
    pytest_socket.disable_socket()


@pytest.fixture
def fixt_test_host():
    return "github.com"
