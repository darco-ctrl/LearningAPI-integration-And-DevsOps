import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts/"

while True:
    user_input_id = input("Enter Id: ")

    if user_input_id.isdigit():
        input_id = int(user_input_id)
        if input_id > 0 and input_id <= 100:
            url = URL + user_input_id

            response = requests.get(url)
            data = response.json()

            while True:
                user_requested_data = input("Enter the data you want to get (userId, id, title, body) 'all' to get all type, 'e' to exit\n: ")

                if user_requested_data == "e":
                    break

                elif user_requested_data == "all":
                    print(json.dumps(data, indent=4))

                elif user_requested_data in data:
                    print(f"{user_requested_data}: {data[user_requested_data]}")

                else:
                    print("Given data type is not avaible please Entre again")
                    continue

        else:
            print(f"Could not find ID: '{input_id}', Please validate your ID and try again")
            continue

    elif user_input_id == "e":
        print("Are you sure you want to exit enter 'Confirm' to exit")
        user_exit_input = input("- ")
        if user_exit_input == "Confirm":
            break
        else:
            continue

    else:
        print(f"Given id '{user_input_id}' is not an integer please enter again\n")
        continue