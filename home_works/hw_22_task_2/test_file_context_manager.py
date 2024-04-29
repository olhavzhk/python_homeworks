import logging
import os
import pytest

from file_context_manager import FileContextManager

logging.disable(logging.CRITICAL)


@pytest.fixture
def temp_file(tmpdir):
    temp_file_path = os.path.join(tmpdir, 'test_file.txt')
    yield temp_file_path
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)


def test_file_context_manager(temp_file):
    with FileContextManager(temp_file, 'w') as f:
        f.write('Test data')

    assert os.path.exists(temp_file)


def test_file_context_manager_multiple_entries(tmp_path):
    temp_file = tmp_path / "test_file.txt"

    with open(temp_file, 'w') as _:
        pass

    with FileContextManager(temp_file, 'w') as f1:
        f1.write('Test data 1')

    with FileContextManager(temp_file, 'a') as f2:
        f2.write('Test data 2')

    with open(temp_file, 'r') as f:
        assert f.read() == 'Test data 1Test data 2'


def test_file_context_manager_exception(temp_file):
    with pytest.raises(Exception):
        with FileContextManager(temp_file, 'r') as f:
            raise Exception('Test exception')

    assert not os.path.exists(temp_file)
