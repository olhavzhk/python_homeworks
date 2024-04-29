import os
import json
import pytest
from phonebook import (
    load_phonebook,
    save_phonebook,
    add_entry,
    search_phonebook,
    delete_entry,
    update_entry,
)


def phonebook_name():
    return "test_phonebook"


def sample_phonebook_data():
    return [
        {
            "first_name": "Michael",
            "last_name": "Scott",
            "full_name": "Michael Scott",
            "phone_number": "1234567890",
            "city_state": "Scranton",
        },
        {
            "first_name": "Dwight",
            "last_name": "Schrute",
            "full_name": "Dwight Schrute",
            "phone_number": "7175550177",
            "city_state": "Scranton",
        },
    ]


def test_load_phonebook():
    phonebook_path = os.path.join(os.path.dirname(__file__), phonebook_name())
    with open(phonebook_path, "w") as file:
        json.dump(sample_phonebook_data(), file)

    actual_result = load_phonebook(phonebook_name())
    expected_result = sample_phonebook_data()
    assert actual_result == expected_result


def test_save_phonebook():
    phonebook_path = os.path.join(os.path.dirname(__file__), phonebook_name())
    save_phonebook(sample_phonebook_data(), phonebook_name())
    expected_result = sample_phonebook_data()

    with open(phonebook_path, "r") as file:
        actual_result = json.load(file)

    assert expected_result == actual_result


def test_add_entry(monkeypatch, capsys):
    inputs = iter(["Jim", "Halpert", "0987654321", "Scranton"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    phonebook = []
    add_entry(phonebook)

    captured = capsys.readouterr()
    assert "Entry added successfully!" in captured.out
    assert len(phonebook) == 1
    assert phonebook[0]["first_name"] == "Jim"
    assert phonebook[0]["last_name"] == "Halpert"
    assert phonebook[0]["full_name"] == "Jim Halpert"
    assert phonebook[0]["phone_number"] == "0987654321"
    assert phonebook[0]["city_state"] == "Scranton"


def test_search_phonebook():
    results = search_phonebook(sample_phonebook_data(), "first_name", "Michael")
    assert results == [sample_phonebook_data()[0]]


def test_delete_entry():
    phonebook = sample_phonebook_data().copy()
    phone_number_to_delete = phonebook[0]["phone_number"]
    delete_entry(phonebook, phone_number_to_delete)
    assert phonebook == [sample_phonebook_data()[1]]


def test_update_entry(monkeypatch, capsys):
    phonebook = sample_phonebook_data().copy()
    phone_number_to_update = phonebook[0]["phone_number"]

    mock_inputs = iter(["Pam", "Beesly", "5705550148", "Scranton"])

    def mock_input(prompt):
        return next(mock_inputs)

    monkeypatch.setattr("builtins.input", mock_input)
    update_entry(phonebook, phone_number_to_update)

    captured = capsys.readouterr()
    assert "Entry updated successfully!" in captured.out
    assert phonebook[0]["first_name"] == "Pam"
    assert phonebook[0]["last_name"] == "Beesly"
    assert phonebook[0]["full_name"] == "Pam Beesly"
    assert phonebook[0]["phone_number"] == "5705550148"
    assert phonebook[0]["city_state"] == "Scranton"


if __name__ == "__main__":
    pytest.main()
