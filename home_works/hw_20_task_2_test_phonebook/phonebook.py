import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
json_phonebook_data = []
converted_object = json.dumps(json_phonebook_data)


def create_phonebook():
    with open(os.path.join(current_dir, "phonebook_data.json"), "w") as data:
        data.write(converted_object)


def load_phonebook(phonebook_name):
    if os.path.exists(f"{phonebook_name}.json"):
        with open(f"{phonebook_name}.json", "r") as file:
            return json.load(file)
    else:
        raise FileNotFoundError("Phonebook not found. Please create a new hw_20_task_2_test_phonebook.")


def save_phonebook(phonebook, phonebook_name):
    with open(f"{phonebook_name}.json", "w") as file:
        json.dump(phonebook, file, indent=4)


def add_entry(phonebook):
    print("Add a new entry to the phonebook:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = f"{first_name} {last_name}"
    phone_number = input("Enter telephone number: ")
    city_state = input("Enter city or state: ")
    entry = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "phone_number": phone_number,
        "city_state": city_state
    }
    phonebook.append(entry)
    print("Entry added successfully!")


def search_phonebook(phonebook, search_key, search_value):
    results = []
    for entry in phonebook:
        if entry.get(search_key) == search_value:
            results.append(entry)
    return results


def delete_entry(phonebook, phone_number):
    for entry in phonebook:
        if entry["phone_number"] == phone_number:
            phonebook.remove(entry)
            print("Entry deleted successfully!")
            return
    print("Entry not found.")


def update_entry(phonebook, phone_number):
    for entry in phonebook:
        if entry["phone_number"] == phone_number:
            print("Update the entry details:")
            entry["first_name"] = input("Enter first name: ")
            entry["last_name"] = input("Enter last name: ")
            entry["full_name"] = f"{entry['first_name']} {entry['last_name']}"
            entry["phone_number"] = input("Enter telephone number: ")
            entry["city_state"] = input("Enter city or state: ")
            print("Entry updated successfully!")
            return
    print("Entry not found.")


def main():
    phonebook_name = input("Enter the name of the hw_20_task_2_test_phonebook: ")
    try:
        phonebook = load_phonebook(phonebook_name)
    except FileNotFoundError as error:
        print(error)
        return
    while True:
        print("\n-- Phonebook Menu --")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record for a given telephone number")
        print("8. Update a record for a given telephone number")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            search_key = "first_name"
            search_value = input("Enter first name to search: ")
            results = search_phonebook(phonebook, search_key, search_value)
            print_results(results)
        elif choice == "3":
            search_key = "last_name"
            search_value = input("Enter last name to search: ")
            results = search_phonebook(phonebook, search_key, search_value)
            print_results(results)
        elif choice == "4":
            search_key = "full_name"
            search_value = input("Enter full name to search: ")
            results = search_phonebook(phonebook, search_key, search_value)
            print_results(results)
        elif choice == "5":
            search_key = "phone_number"
            search_value = input("Enter telephone number to search: ")
            results = search_phonebook(phonebook, search_key, search_value)
            print_results(results)
        elif choice == "6":
            search_key = "city_state"
            search_value = input("Enter city or state to search: ")
            results = search_phonebook(phonebook, search_key, search_value)
            print_results(results)
        elif choice == "7":
            phone_number = input("Enter telephone number to delete: ")
            delete_entry(phonebook, phone_number)
        elif choice == "8":
            phone_number = input("Enter telephone number to update: ")
            update_entry(phonebook, phone_number)
        elif choice == "9":
            save_phonebook(phonebook, phonebook_name)
            print("Phonebook saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def print_results(results):
    if results:
        print("\nSearch Results:")
        for entry in results:
            print(f"First Name: {entry['first_name']}")
            print(f"Last Name: {entry['last_name']}")
            print(f"Telephone Number: {entry['phone_number']}")
            print(f"City or State: {entry['city_state']}")
            print("--------------------------")
    else:
        print("No results found.")


if __name__ == "__main__":
    main()
