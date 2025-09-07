import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts/"

id_file = open("caches\\ids.json")
id_data_str = id_file.read()
ids_json_data = json.loads(id_data_str)

while True:
    input_id_str = input("Enter Id: ")

    if input_id_str.isdigit():
        input_id_int = int(input_id_str)
        if input_id_int > 0 and input_id_int <= 100:
            url = URL + input_id_str

            if input_id_str in ids_json_data:
                data = ids_json_data[input_id_str]

            else:
                response = requests.get(url)
                data = response.json()

                ids_json_data[str(data["id"])] = {
                    "userId": data["userId"],
                    "title": data["title"],
                    "body": data["body"]
                }

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
            print(f"Could not find ID: '{input_id_int}', Please validate your ID and try again")
            continue

    elif input_id_str == "e":
        print("Are you sure you want to exit enter 'Confirm' to exit")
        user_exit_input = input("- ")
        if user_exit_input == "Confirm":
            break
        else:
            continue

    else:
        print(f"Given id '{input_id_str}' is not an integer please enter again\n")
        continue

json_file = open("caches\\ids.json", 'w')
json.dump(ids_json_data, json_file)