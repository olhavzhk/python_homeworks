import pytest
from tv_controller import TVController

CHANNELS = ["BBC", "Discovery", "TV1000"]


def test_first_channel():
    controller = TVController(CHANNELS)
    assert controller.first_channel() == "BBC"


def test_last_channel():
    controller = TVController(CHANNELS)
    assert controller.last_channel() == "TV1000"


def test_turn_channel():
    controller = TVController(CHANNELS)
    assert controller.turn_channel(1) == "BBC"
    assert controller.turn_channel(2) == "Discovery"
    assert controller.turn_channel(4) == "Channel not found"


def test_next_channel():
    controller = TVController(CHANNELS)
    assert controller.next_channel() == "Discovery"
    controller.turn_channel(3)
    assert controller.next_channel() == "BBC"


def test_previous_channel():
    controller = TVController(CHANNELS)
    assert controller.previous_channel() == "TV1000"
    controller.turn_channel(3)
    assert controller.previous_channel() == "Discovery"


def test_current_channel():
    controller = TVController(CHANNELS)
    assert controller.current_channel() == "BBC"
    controller.turn_channel(2)
    assert controller.current_channel() == "Discovery"


def test_is_exist():
    controller = TVController(CHANNELS)
    assert controller.is_exist(1) == "Yes"
    assert controller.is_exist("BBC") == "Yes"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("BBC") == "Yes"


if __name__ == "__main__":
    pytest.main()
