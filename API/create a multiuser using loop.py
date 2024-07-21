import requests
import json

# Base URL:
base_url = "https://reqres.in/api"

# Auth key
auth_token = "token ...token value"

# Post request function
def post_request(user_names, loop=10):
    url = base_url + "/users/"
    print("Post url : ", url)
    headers = {"Authorization": auth_token}
    all_user_ids = []

    for i in range(loop):
        print(f"--- loop {i + 1} ---")
        user_ids = []

        for name in user_names:
            data = {
                "name": name,
                "job": "QA Learner"
            }
            response = requests.post(url, json=data, headers=headers)
            json_data = response.json()
            json_str = json.dumps(json_data, indent=6)
            print("Json data post response:", name, ":", json_str)
            user_id = json_data.get("id")
            if user_id:
                user_ids.append(user_id)
            assert response.status_code == 201
            assert "name" in json_data
            print(".........Post/user is created successfully", name, ".............")

        all_user_ids.extend(user_ids)
        print(f"User IDs created in loop {i + 1}: {user_ids} ")

    return all_user_ids

# User name example:
user_names = ["Surakshya", "Sita", "Gita", "Hari", "Ram", "Shyam", "Radha","Krishna", "Manoj","Manisha"]
all_user_ids = post_request(user_names)
print("All created user IDs:", all_user_ids)
